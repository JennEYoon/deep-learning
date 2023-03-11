# Transformers p 626-629, chp 16

Oct 2020, Google: Alexey Dosovitskiy et al., "An Image Is Worth 16x16 Words: Transformers for Image Recognition at Scale"  

Vision Transformer (ViT). 
"The idea is surprisingly simple: just chop the image into little 16x16 squares."  
 * flatten 16x16x3 = 768 dim vector. 
 * pas through linear layer to transform each vector, but retain dimentional information
 * sequence of resulting vectors treated like sequence of word embeddings.  
 * (add positional embeddings and pass through the transformer model.



