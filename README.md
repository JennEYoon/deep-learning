# My practice repo for deep-learning.  

***Note: Renamed "master" to "main" branch in June 2020***

Created: May 22, 2020  
Author: Jennifer E. Yoon

---  

### I. NVIDIA deep learning book  

  * Magnus Ekman, Learning Deep Learning, NVIDIA Deep Learning Institute, c 2022 NVIDIA Corp., Addison-Wesley publishing

   Has extremely good explanations of math and concepts with colored charts. Cheatsheet at the end of the book organizes the different DL models and how to use them. It's not a beginner book. Intermediate to advanced book, in my opinion.  Better than Chollet book 2nd ed.  Has more complete details.  Subtitle is Theory and Practice of Neural Networks, Computer Vision, Natural Language Processing, and Transformers using TensorFlow.  This is a good description of the subject matter.  I don't know what transformers are in deep learning, so that will be interesting.  Appendix has PyTorch vs TensorFlow chart for how to convert your project code between these two libraries.   



### II. My exercises from Chollet, Deep Learning with Python book, 2nd ed, c 2011 Nov.    

  * Chp 1 and 2 for small group, Oct 25, 2021, Monday.  
    Peter, Dan, me, and Elaheh  
    
    ---  

#### First edition notes:  

  * Appendix: setup, tensorflow, keras, GPU on AWS EC2.   
    AWS EC2 GPU large instance still too expensive in May 2020, 70 cents/hour.    
    Use Google Colab free GPU instances instead. (My free $300 credit expired unused in April 2020.)  
  
  * Chp 4.5: Universal Workflow of Deep Learning  
  
  * Chp 5: Convolutional Networks -- has vision recognition examples.  
  
  * Chp 8 & 9: Generative Deep Learning, Conclusion  
    Has interesting examples, deep dream, art style transfer, face genereration.  Look forward to future research.  Limitations of deep learning.  

### III. fast.ai 2020 class, fastai v2 package, Practical Deep Learning for Coders:  

***Moved to "fastai-dl-study" repo in Oct 2021*** 
https://github.com/JennEYoon/fastai-dl-study/tree/main/fastbook  

  * Class part 1, March 2020: https://course.fast.ai/  
  * Book on Amazon:  https://www.amazon.com/Deep-Learning-Coders-fastai-PyTorch/dp/1492045527/ref=sr_1_1?dchild=1&keywords=fastai&qid=1601497208&sr=8-1  
  * Full book in nbs:  https://github.com/fastai/fastbook  
  * Download fastai v2 package: https://github.com/fastai/fastai  

#### My revisit of fast.ai deep learning classes in August 2020:  
Back in 2018 when I first came across fast.ai, it was too hard for me to work through the notebooks because I didn't have the minimum required 1 year of focused coding experience in any language.  I came across Jeremy Howard's interviews on YouTube, and it peaked my interest again.  Now might be a good time to pick this up again.  There is also fastai book which is a new development.  It seems to be a condensed and coordinated version of the video lectures and a good reference. The book also covers part II, fundamentals of deep learning, and some of their basic machine learning class.  

---  
  
### IV. Other:  

 * Goodfellow et al, Deep Learning book  
   https://www.deeplearningbook.org/  

---  

###  V. Setup, Environment:  

  * I use conda env "dlpy" on Ubuntu (WSL), CPU x86 laptop:  
    Ubuntu-side "dlpy" env has python v 3.8, tensorflow v 2.2 installed using pip.  
  * PyTorch v 1.6 stable also installed to "dlpy" env on Ubuntu (WSL).  
