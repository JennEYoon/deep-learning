# Talking points, Chollet, chp 12  

### Wednesday July 6, 2022 small group, 7 pm virtual  

Part 1 - text gen:  
Continuation of Transformer model from chp 11 end.  
Sequent to sequence, pre-trained encoder and language model?  
Decoder to generate possible sentences from IMDB move reviews inputs.  
Randomness variable set to 0.2, 0.5, 0.7, 1.0, 1.5, larger number introduces more randomness.  



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

part 4 variational autoencoder  
conceptual encoding space in muti axes.  
face transform along a conceptual "smile" axis.  
Smoothly transform resting face to wide smile face, from resting space to horror face.  

part 4 GAN  

Generator gets a 2nd hand representation of training images via discriminator's feedback.  
Generator is like a blind folded person who can find the target via respompnse from sighted players in a game.  Marco Polo, pinatta, pin the donkey.  






