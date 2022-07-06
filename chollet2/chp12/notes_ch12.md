# Talking points, Chollet, chp 12  

### Wednesday July 6, 2022 small group, 7 pm virtual  

Part 1 - text gen:  
Continuation of Transformer model from chp 11 end.  
Sequent to sequence, pre-trained encoder and language model?  
Decoder to generate possible sentences from IMDB move reviews inputs.  
Randomness variable set to 0.5, 1.7, 2.5 ?



Part 2 - Deep Dream:  
Reference picture 
 + modified by style vector  
   - earlier layer is texture  
   - later layer is larger structures, combination of earlier layers. 
Inception model, resize from small to large several times.  
Trained on small image size. If applied to large reference image without resizing, result will be very small.  
Recursively resize, so chosen texture/pattern can be reapplied at different scales, make it more trippy.  
Trained on ImageNet, so have lots of dogs, cats, buildings, etd.  
This will come through in the final picture.  
Can use model trained on other objects, people's faces, to have more targeted application.
   
   

Part 3 - Style Transfer:  

angram?  
Reference picture 
+ Style from layer 1 of each level, texture more than larger structures.  
= output images.  





