# AIMA Chp 24 NLP and Chp 25 DL for NLP  

### Chp 25 Deep Learning for Natural Language Processing  
June 1,2022:   
Reading chp 25, interesting explanation or NLP, has Transformers explanation.  
To keep notes here.  

Embedding matrix is a sparse representation of V words X N features.  
Embedding matrix is learning.  Uses n-gram.  Idea that similar words are close together in occurence.  
Don't know how, but model seems to catch features of words that stands for similar items like country, parts of speech (verb, adjetive, past tense, present tense), colors, weather, siblings, etc.  

These are not one-hot encoding (one 1 and all 0s), because that will be huge matrix.  
100,000 5-gram words requre 10^25 power matrix.  I don't know how that was calculated.  

The 5-input words are fed into 5-hidden layers.  3 levels of hidden layers and one activation function is learning together.  
Initially, Embedding matrix is random numbers, or pretrained weights from Word2Vec or Glove, etc.  

RNN part - middle layer feeds previous word to each word node, until all words have been seen by all nodes.  
Then the middle word parts-of-speech task is output.  
This method is good for downstream tasks, but not good for training initial language model.  Does not guarantee a particular feature will be learned given a particular vocabulary, word corpus 100,000 example.  

### Chp 24 Natural Language Processing:  

First talks about manually creating language model using rules, without machine learning.  

