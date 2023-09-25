# My practice repo for deep-learning.  

Created: May 22, 2020  
Author: Jennifer E. Yoon  


The purpose of this repositories is to assist my study of machine learning and deep learning.  The following are the books and courses I am studying.  I reproduce the code in the books and try my own tweaks and alternative examples.  I also expand upon the examples in the book by using alternative data and running alternative experiments.  .  
.   I am a member of local Meetups in Virginia, USA, where we study machine learning and deep learning together.  


### I. Aurelien Geron, Handson-on Machine Learning, 3rd ed, c 2023  (Oct 2022 printed)  
/geron-ml3/ 

  * Started studying this book with my small group in March 2023. 
  * Very good classic ML chapters in part 1. Good review of code examples.  
  * To expand each notebook with my own data and code.    
  * Much fuller RNN section than Chollet. DL chapters generally have more explanation than Chollet.  
  * Good addition to Cholett book.  .     


### II.  My exercises from Chollet, Deep Learning with Python, 2nd ed, c 2021       
/chollet2/

  * Manning book:  https://www.manning.com/books/deep-learning-with-python-second-edition  
  * Github repo:  https://github.com/fchollet/deep-learning-with-python-notebooks  
  * Best chapter was 12, Generative Models. Is largely unchanged from 1st ed.  
  * Transformers section insufficient. Suppliment with many other sources, esp. image transformers.  
  * Chp 10, 11 examples not good at demonstrating concepts. Not sure what temperature readings from one location show about doing time-series. Results underwhelming. Text generation example not as good as other sources. Results also underwhelming.  
  * Chp 5 encoding, chp 9 advanced vision CNN - most important at concepts, other than 12 (review encoding in VAR).  Text generation works better at fictitious Shakespear's sonnet, as seen in others peoples' examples. RNN is punted mostly. See A. Geron book for fuller treatment. RNN is still useful for games, e.g. Pong, Chess.  
  * Chp 9 repeat April 2023 w DSML Meetup, see Matt Kehoe nb for 9.4. Review this code. 
  * Chp 6, 7, 8 - house keeping, how to use Keras. Looked over once, but later review when needed.    
  * Chp 11 minor code errors, old unsupported command, typo function call, encoder not in same notebook as decoder. Colab only loads one notebook at a time, so all sections need to be in one Jupyter Notebook.  
  * Chp 1 exaggerates user numbers for Keras library relative to other Python libraries using a Kaggle 2021 user survey. Unnecessary since Keras is a foundational library in Python deep learning. 
Most users in the survey never entered a Kaggle challenge and never ran a deep learning model, so the results were heavily skewed towards newbies. Then he eliminated Scikit-Learn, which should have been a clear winner. Also PyTorch and Fastai libraries should have been in the running along with Tensorflow and Keras, but is not there.  
  * San Diego Machine Learning meetup group on YouTube discuss all 19 chapters of 2nd ed book. Very similar to 3rd ed chp 1-13.  

### IIb. selected chapters, NVIDIA deep learning book  
/ekman-ldl/

  * Magnus Ekman, Learning Deep Learning, NVIDIA Deep Learning Institute, c 2022 NVIDIA Corp., Addison-Wesley publishing

Has extremely good explanations of math and concepts with colored charts. Cheatsheet at the end of the book organizes the different DL models and how to use them. It's not a beginner book. Intermediate to advanced book, in my opinion.  Better than Chollet book 2nd ed.  Has more complete details.  Subtitle is Theory and Practice of Neural Networks, Computer Vision, Natural Language Processing, and Transformers using TensorFlow.  This is a good description of the subject matter.  Appendix has PyTorch vs TensorFlow chart for how to convert your project code between these two libraries. PyTorch version of all chapter code is available online.  NVIDIA GTC conference in 2021 and 2022 demo the book in a tutorial.  To download PyTorch notebooks and try 


### III. Practical Deep Learning for Coders, fastai 

***Moved to "fastai-deep-learning" repo in Oct 2021***  

### IV.  Coursera Deep Learning Specialization classes  

***Move to "Coursera-DLAI" repo in Oct 2020***  

### V.  Udemy Python Machine Learning class, by Jose Portia   
 See learn-ml repo

---  

###  V. Setup, Environment:  

  * New setup, RTX 3070 GPU laptop, June 2022:  
    Windows 10 with WSL2 Ubuntu 20.4  
    miniconda3 on WSL2 Ubuntu
    conda env base - Tensorflow v 2.6, Cuda toolkit, Cuda gpu drivers, python v 3.8.  
       - note NVIDIA GPU driver version and Cude toolkit version must ve compatible with Tensorflow version installed,  
       - Nvidea provides a table to check.
    conda env dl - Pytorch, fastai v2, Python v3.7 (for Chollet 2nd ed book)
    VS Code with Python v3.10 extension installed on Windows side (for wsl and windows use)    
     * Laptop notes: only 6GB VRAM, limits batch size and image pixel size. Class examples are fine.  
        - RTX 3070 Laptop GPU - sweet spot in power consumption, price, speed.  
        - Equivalent to Colab GPU 2nd level, 90% faster than 1st level GPU (P100) on language models.  
    2nd miniconda3 on C:/python/conda3/ Windows 10 OS.  
    conda base env has basic ML/DL libraries, python version 3.9.   

  * 2nd CPU laptop:  I use conda env "dlpy" on Ubuntu (WSL), CPU x86 laptop:  
    Ubuntu-side "dlpy" env has python v 3.8, tensorflow v 2.2 installed using pip.  
  * PyTorch v 1.6 stable also installed to "dlpy" env on Ubuntu (WSL).  

  * VS Code installed on Windows, Python extension also installed on C:/python drive.  
  * Miniconda3 windows version installed on C drive, Python version 3.9 base environment.  
    - Use with code on C drive.  


### VI. Git repo cleanup, history:  

 On 6/25/2022 performed git repo history cleanup. Remove deleted folders & large files from git commit history.
 * Successfully reduced repo size from 1.3 GB to under 500 MB.   
 * Removed empty commits related to deleted folders and deleted large files. Commit history number for repo declined, as expected.    
 * Unexpectedly increased total number of commits on github commit history graph by 900 in 2020 and 600 in 2021.  No fix.  Seems to be Github error.  
 * Hard reset on Github, delete existing repo, then create fresh repo with same name, push from local to Github.  Fixed weird problem with too many extra commits on GITHUB commit history graph, but lost a few stars and forks from other users who had been following this repo.  
 * Decided to make this trade off.   
 
---  

###  VII. License - Apache 2.0  

   Copyright 2020-2023 by Jennifer E. Yoon

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.Vi. 

