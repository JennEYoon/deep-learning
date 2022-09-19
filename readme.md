# My practice repo for deep-learning.  

Created: May 22, 2020  
Author: Jennifer E. Yoon  

Git history cleanup, remove deleted folders/large files from git history on 6/25/2022
 * Successfully reduced repo size from 1.3 GB to under 500 MB.   
 * Removed empty commits related to deleted folders and deleted large files. Commit history number for repo declined, as expected.    
 * Unexpectedly increased total number of commits on github commit history graph by 900 in 2020 and 600 in 2021.  No fix.  Seems to be Github error.  
 * Hard reset on Github, delete existing repo, then create fresh repo with same name, push from local to Github.  Fixed weird problem with too many extra commits on GITHUB commit history graph, but lost a few stars and forks from other users who had been following this repo.  
 * Decided to make the trade off.   
 
---  

### I. NVIDIA deep learning book  

  * Magnus Ekman, Learning Deep Learning, NVIDIA Deep Learning Institute, c 2022 NVIDIA Corp., Addison-Wesley publishing

Has extremely good explanations of math and concepts with colored charts. Cheatsheet at the end of the book organizes the different DL models and how to use them. It's not a beginner book. Intermediate to advanced book, in my opinion.  Better than Chollet book 2nd ed.  Has more complete details.  Subtitle is Theory and Practice of Neural Networks, Computer Vision, Natural Language Processing, and Transformers using TensorFlow.  This is a good description of the subject matter.  I don't know what transformers are in deep learning, so that will be interesting.  Appendix has PyTorch vs TensorFlow chart for how to convert your project code between these two libraries.   


### II. My exercises from Chollet, Deep Learning with Python, 2nd ed, c 2021       

 * Manning book:  https://www.manning.com/books/deep-learning-with-python-second-edition  
 * Github repo:  https://github.com/fchollet/deep-learning-with-python-notebooks  

### III. Practical Deep Learning for Coders, fastai 

***Moved to "fastai-deep-learning" repo in Oct 2021***  

### IV.  Coursera Deep Learning Specialization classes  

***Move to "Coursera-DLAI" repo in Oct 2020***  

---  

###  V. Setup, Environment:  

  * New setup, RTX 3070 GPU laptop, June 2022:  
    Windows 10 with WSL2 Ubuntu 20.4  
    miniconda3 on WSL2 Ubuntu
    conda env base - Tensorflow v 2.6, Cuda toolkit, Cuda gpu drivers, python v 3.8.  
       - note NVIDIA GPU driver version and Cude toolkit version must ve compatible with Tensorflow version installed,  
       - Nvidea provides a table to check.
    conda env dl - Pytorch, fastai v2, Python v3.7
    VS Code with Python v3.10 extension installed on Windows side (for wsl and windows use)    

  * I use conda env "dlpy" on Ubuntu (WSL), CPU x86 laptop:  
    Ubuntu-side "dlpy" env has python v 3.8, tensorflow v 2.2 installed using pip.  
  * PyTorch v 1.6 stable also installed to "dlpy" env on Ubuntu (WSL).  

  * VS Code installed on Windows, Python extension also installed on C:/python drive.  
  * Minicomda3 windows installed on C drive, python version 3.9 base environment.  

###  VI. License - Apache 2.0  

   Copyright 2020-2022 by Jennifer E. Yoon

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.Vi. 

