# -*- coding: utf-8 -*-
"""c15_10.Bach_PyTorch.py

PyTorch version of Bach Chorales generation
Claude free Sonnet 4

## 10. Bach Chorales
Exercise: Download the Bach chorales dataset and train a PyTorch model 
that can predict the next time step (four notes), given a sequence of 
time steps from a chorale.
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import torch.nn.functional as F

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path
import requests
import tarfile
import os

# Download and extract the dataset
def download_bach_dataset():
    url = "https://github.com/ageron/data/raw/main/jsb_chorales.tgz"
    filepath = "jsb_chorales.tgz"
    
    if not os.path.exists("jsb_chorales"):
        print("Downloading Bach chorales dataset...")
        response = requests.get(url)
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        # Extract the tar file
        with tarfile.open(filepath, 'r:gz') as tar:
            tar.extractall('.')
        
        os.remove(filepath)
        print("Dataset downloaded and extracted.")
    
    return Path("jsb_chorales")

jsb_chorales_dir = download_bach_dataset()

train_files = sorted(jsb_chorales_dir.glob("train/chorale_*.csv"))
valid_files = sorted(jsb_chorales_dir.glob("valid/chorale_*.csv"))
test_files = sorted(jsb_chorales_dir.glob("test/chorale_*.csv"))

def load_chorales(filepaths):
    return [pd.read_csv(filepath).values.tolist() for filepath in filepaths]

train_chorales = load_chorales(train_files)
valid_chorales = load_chorales(valid_files)
test_chorales = load_chorales(test_files)

print(f"First chorale sample: {train_chorales[0][:5]}")

# Find note range
notes = set()
for chorales in (train_chorales, valid_chorales, test_chorales):
    for chorale in chorales:
        for chord in chorale:
            notes |= set(chord)

n_notes = len(notes)
min_note = min(notes - {0})
max_note = max(notes)

print(f"Note range: {min_note} to {max_note}, total notes: {n_notes}")

# Audio synthesis functions (unchanged from original)
from IPython.display import Audio

def notes_to_frequencies(notes):
    return 2 ** ((np.array(notes) - 69) / 12) * 440

def frequencies_to_samples(frequencies, tempo, sample_rate):
    note_duration = 60 / tempo
    frequencies = (note_duration * frequencies).round() / note_duration
    n_samples = int(note_duration * sample_rate)
    time = np.linspace(0, note_duration, n_samples)
    sine_waves = np.sin(2 * np.pi * frequencies.reshape(-1, 1) * time)
    sine_waves *= (frequencies > 9.).reshape(-1, 1)
    return sine_waves.reshape(-1)

def chords_to_samples(chords, tempo, sample_rate):
    freqs = notes_to_frequencies(chords)
    freqs = np.r_[freqs, freqs[-1:]]
    merged = np.mean([frequencies_to_samples(melody, tempo, sample_rate)
                     for melody in freqs.T], axis=0)
    n_fade_out_samples = sample_rate * 60 // tempo
    fade_out = np.linspace(1., 0., n_fade_out_samples)**2
    merged[-n_fade_out_samples:] *= fade_out
    return merged

def play_chords(chords, tempo=160, amplitude=0.1, sample_rate=44100, filepath=None):
    samples = amplitude * chords_to_samples(chords, tempo, sample_rate)
    if filepath:
        from scipy.io import wavfile
        samples = (2**15 * samples).astype(np.int16)
        wavfile.write(filepath, sample_rate, samples)
        return Audio(filepath)
    else:
        return Audio(samples, rate=sample_rate)

# Test audio with first few chorales
print("Playing first 3 chorales...")
for index in range(3):
    display(play_chords(train_chorales[index]))

# PyTorch Dataset class
class BachDataset(Dataset):
    def __init__(self, chorales, window_size=32, window_shift=16):
        self.window_size = window_size
        self.window_shift = window_shift
        self.min_note = min_note
        
        # Preprocess all chorales into windows
        self.windows = []
        for chorale in chorales:
            # Convert chorale to arpegio (flatten chords to sequence of notes)
            arpegio = []
            for chord in chorale:
                arpegio.extend(chord)
            
            # Shift note values (0 stays 0, others become 1-46)
            arpegio = [0 if note == 0 else note - self.min_note + 1 for note in arpegio]
            
            # Create sliding windows
            for i in range(0, len(arpegio) - window_size, window_shift):
                if i + window_size + 1 <= len(arpegio):
                    window = arpegio[i:i + window_size + 1]
                    self.windows.append(window)
    
    def __len__(self):
        return len(self.windows)
    
    def __getitem__(self, idx):
        window = self.windows[idx]
        x = torch.tensor(window[:-1], dtype=torch.long)
        y = torch.tensor(window[1:], dtype=torch.long)
        return x, y

# Create datasets
train_dataset = BachDataset(train_chorales)
valid_dataset = BachDataset(valid_chorales)
test_dataset = BachDataset(test_chorales)

# Create data loaders
batch_size = 32
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
valid_loader = DataLoader(valid_dataset, batch_size=batch_size, shuffle=False)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

print(f"Dataset sizes - Train: {len(train_dataset)}, Valid: {len(valid_dataset)}, Test: {len(test_dataset)}")

# PyTorch Model
class BachModel(nn.Module):
    def __init__(self, n_notes, n_embedding_dims=5):
        super(BachModel, self).__init__()
        
        # Embedding layer
        self.embedding = nn.Embedding(n_notes, n_embedding_dims)
        
        # Convolutional layers (WaveNet-like)
        self.conv1 = nn.Conv1d(n_embedding_dims, 32, kernel_size=2, dilation=1, padding=1)
        self.bn1 = nn.BatchNorm1d(32)
        
        self.conv2 = nn.Conv1d(32, 48, kernel_size=2, dilation=2, padding=2)
        self.bn2 = nn.BatchNorm1d(48)
        
        self.conv3 = nn.Conv1d(48, 64, kernel_size=2, dilation=4, padding=4)
        self.bn3 = nn.BatchNorm1d(64)
        
        self.conv4 = nn.Conv1d(64, 96, kernel_size=2, dilation=8, padding=8)
        self.bn4 = nn.BatchNorm1d(96)
        
        # LSTM layer
        self.lstm = nn.LSTM(96, 256, batch_first=True)
        
        # Output layer
        self.output = nn.Linear(256, n_notes)
        
        self.dropout = nn.Dropout(0.1)
        
    def forward(self, x):
        # Embedding
        x = self.embedding(x)  # (batch, seq_len, embedding_dim)
        
        # Transpose for Conv1d (batch, channels, seq_len)
        x = x.transpose(1, 2)
        
        # Convolutional layers with causal padding
        x = F.relu(self.bn1(self.conv1(x)))
        x = x[:, :, :-1]  # Remove last timestep for causal
        
        x = F.relu(self.bn2(self.conv2(x)))
        x = x[:, :, :-2]  # Remove padding for causal
        
        x = F.relu(self.bn3(self.conv3(x)))
        x = x[:, :, :-4]  # Remove padding for causal
        
        x = F.relu(self.bn4(self.conv4(x)))
        x = x[:, :, :-8]  # Remove padding for causal
        
        # Transpose back for LSTM (batch, seq_len, channels)
        x = x.transpose(1, 2)
        
        # LSTM
        x, _ = self.lstm(x)
        x = self.dropout(x)
        
        # Output layer
        x = self.output(x)
        
        return x

# Initialize model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

model = BachModel(n_notes).to(device)
print(f"Model parameters: {sum(p.numel() for p in model.parameters())}")

# Training setup
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=1e-3)

# Training function
def train_epoch(model, train_loader, criterion, optimizer, device):
    model.train()
    total_loss = 0
    correct = 0
    total = 0
    
    for batch_idx, (data, targets) in enumerate(train_loader):
        data, targets = data.to(device), targets.to(device)
        
        optimizer.zero_grad()
        outputs = model(data)
        
        # Reshape for loss calculation
        outputs = outputs.view(-1, outputs.size(-1))
        targets = targets.view(-1)
        
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()
        
        total_loss += loss.item()
        pred = outputs.argmax(dim=1)
        correct += pred.eq(targets).sum().item()
        total += targets.size(0)
        
        if batch_idx % 100 == 0:
            print(f'Batch {batch_idx}/{len(train_loader)}, Loss: {loss.item():.4f}')
    
    return total_loss / len(train_loader), correct / total

# Validation function
def validate(model, valid_loader, criterion, device):
    model.eval()
    total_loss = 0
    correct = 0
    total = 0
    
    with torch.no_grad():
        for data, targets in valid_loader:
            data, targets = data.to(device), targets.to(device)
            outputs = model(data)
            
            outputs = outputs.view(-1, outputs.size(-1))
            targets = targets.view(-1)
            
            loss = criterion(outputs, targets)
            total_loss += loss.item()
            
            pred = outputs.argmax(dim=1)
            correct += pred.eq(targets).sum().item()
            total += targets.size(0)
    
    return total_loss / len(valid_loader), correct / total

# Training loop
epochs = 20
train_losses = []
valid_losses = []

print("Starting training...")
for epoch in range(epochs):
    print(f'\nEpoch {epoch + 1}/{epochs}')
    
    train_loss, train_acc = train_epoch(model, train_loader, criterion, optimizer, device)
    valid_loss, valid_acc = validate(model, valid_loader, criterion, device)
    
    train_losses.append(train_loss)
    valid_losses.append(valid_loss)
    
    print(f'Train Loss: {train_loss:.4f}, Train Acc: {train_acc:.4f}')
    print(f'Valid Loss: {valid_loss:.4f}, Valid Acc: {valid_acc:.4f}')

# Save model
torch.save(model.state_dict(), 'bach_model_pytorch.pth')
print("Model saved!")

# Test the model
test_loss, test_acc = validate(model, test_loader, criterion, device)
print(f'Test Loss: {test_loss:.4f}, Test Acc: {test_acc:.4f}')

# Generation functions
def preprocess_seed(seed_chords):
    """Convert seed chords to arpegio format for generation"""
    arpegio = []
    for chord in seed_chords:
        arpegio.extend(chord)
    # Shift note values
    arpegio = [0 if note == 0 else note - min_note + 1 for note in arpegio]
    return torch.tensor(arpegio, dtype=torch.long).unsqueeze(0)

def postprocess_arpegio(arpegio):
    """Convert arpegio back to chords"""
    # Shift notes back
    arpegio = arpegio.squeeze(0).cpu().numpy()
    arpegio = [0 if note == 0 else note + min_note - 1 for note in arpegio]
    
    # Reshape to chords (4 notes per chord)
    n_chords = len(arpegio) // 4
    chords = np.array(arpegio[:n_chords * 4]).reshape(-1, 4)
    return chords.tolist()

def generate_chorale(model, seed_chords, length, device):
    """Generate chorale deterministically (always picks highest probability)"""
    model.eval()
    arpegio = preprocess_seed(seed_chords).to(device)
    
    with torch.no_grad():
        for chord in range(length):
            for note in range(4):
                outputs = model(arpegio)
                next_note = outputs[0, -1, :].argmax().unsqueeze(0).unsqueeze(0)
                arpegio = torch.cat([arpegio, next_note], dim=1)
    
    return postprocess_arpegio(arpegio)

def generate_chorale_v2(model, seed_chords, length, temperature=1.0, device=device):
    """Generate chorale with temperature sampling"""
    model.eval()
    arpegio = preprocess_seed(seed_chords).to(device)
    
    with torch.no_grad():
        for chord in range(length):
            for note in range(4):
                outputs = model(arpegio)
                logits = outputs[0, -1, :] / temperature
                probabilities = F.softmax(logits, dim=0)
                next_note = torch.multinomial(probabilities, 1).unsqueeze(0)
                arpegio = torch.cat([arpegio, next_note], dim=1)
    
    return postprocess_arpegio(arpegio)

# Test generation
seed_chords = test_chorales[2][:8]
print("Playing seed chords...")
display(play_chords(seed_chords, amplitude=0.2))

# Generate deterministic chorale
print("Generating deterministic chorale...")
new_chorale = generate_chorale(model, seed_chords, 56, device)
display(play_chords(new_chorale))

# Generate chorales with different temperatures
print("Generating chorales with temperature sampling...")

new_chorale_cold = generate_chorale_v2(model, seed_chords, 56, temperature=0.8, device=device)
display(play_chords(new_chorale_cold, filepath="bach_cold_pytorch.wav"))

new_chorale_medium = generate_chorale_v2(model, seed_chords, 56, temperature=1.0, device=device)
display(play_chords(new_chorale_medium, filepath="bach_medium_pytorch.wav"))

new_chorale_hot = generate_chorale_v2(model, seed_chords, 56, temperature=1.5, device=device)
display(play_chords(new_chorale_hot, filepath="bach_hot_pytorch.wav"))

# Play original test chorale for comparison
print("Playing original test chorale for comparison...")
display(play_chords(test_chorales[2][:64], filepath="bach_test_original.wav"))

print("Bach chorale generation complete! Try different seeds and temperatures to create your masterpiece!")