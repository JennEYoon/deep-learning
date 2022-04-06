# %%
# Interactive Mode 
# Chp 8, Load Image Files, Eckman 

import numpy as np
from tensorflow.keras.applications import resnet50
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.resnet50 import \
    decode_predictions
import matplotlib.pyplot as plt
import tensorflow as tf
#tf.get_logger().setLevel()

# %%

# Load Image, test pictures from local repo  
image = load_img('./data/cats/cat1.jpg', target_size=(224, 224))
# %%
image
# %%
image = load_img('./data/cats/cat2.jpg', target_size=(224, 224))
# %%
image
# %%
image = load_img('./data/dogs/dog2.jpg', target_size=(224, 224))
# %%
image
# %%
image = load_img('./data/dogs/dog1.jpg', target_size=(224, 224))
image
# %%

# %%
