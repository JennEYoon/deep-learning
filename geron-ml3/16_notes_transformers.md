# Transformers p 626-629, chp 16

Oct 2020, Google: Alexey Dosovitskiy et al., "An Image Is Worth 16x16 Words: Transformers for Image Recognition at Scale"  

Vision Transformer (ViT). 
"The idea is surprisingly simple: just chop the image into little 16x16 squares."  
 * flatten 16x16x3 = 768 dim vector. 
 * pass through linear layer to transform each vector, but retain dimentional information
 * sequence of resulting vectors treated like sequence of word embeddings.  
 * (add positional embeddings) and pass the result through the transformer.

Original ViT not as efficient as CNN, used 300 million additional images to train.  
CNNs implicitly assume that patterns learned in one location will likely be useful in other locations as well. 
Inductive bias - implicit assumption made by the model. 

Data efficient image transformers (DeiTs)  Dec 2020, Facebook, Hugo Touvron et al.

OpenAI 2021 CLIP - large pretrained model, match caption to images 
OpenAI DALL.E, DALL.E-2 - image generation diffusion model, high quality
April 2022 DeepMind, Flamingo - multi-modal model  
May 2022 DeepMind GATO, multi-modal, reinforcement learning. chat, play Atari games, control robot arm, caption images. 

### 3Blue 1Brown  
Transformer videos: 
Chp 5 Transformers: https://www.youtube.com/watch?v=wjZofJX0v4M&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi&index=6  
Chp 6 Attention: https://github.com/JennEYoon/deep-learning/blob/main/geron-ml3/Dir_EmbSp_have_meaning_1301.3781v3.pdf  

Ealier paper, directions in embedding space has meaning.  
<a href="https://github.com/JennEYoon/deep-learning/blob/main/geron-ml3/Dir_EmbSp_have_meaning_1301.3781v3.pdf" >paper</a>

Jay Alammar blog, Illustrated Transformer (good for understanding)  


