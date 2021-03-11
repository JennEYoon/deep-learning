# My exercises for Chollet, Deep Learning with Python book  

#### May 10, 2020 notes  
  * Chapter 3)  
    - Use AWS p2.xlarge instance, AMI pre-formatted. $0.90 per hr as of 2017.  
      Can get expensive. Setup with tensorflow, keras and dependencies.  
      (***t2.micro*** instance is free tier.  NOT GPU, vCPU only.)   
      
    - Same price as of May 10, 2020, 90 cents/hr for ***p2.xlarge GPU w 4 cores***.  
    - Cheapest GPU is 52 cents/hr.  
      GPU/vCPU   ECU   Memory ... price per hour.  
      <img src="https://github.com/JennEYoon/learn-mldl/blob/master/books/exercises/chollet-dlwp/AWS-pricing-GPU-2020.png" alt="AWS GPU prices" />
      AWS Free Tier includes 750 hours of Linux and Windows t2.micro instances each month for one year. To stay within the Free Tier, use only EC2 Micro instances.
View AWS Free Tier Details »  https://aws.amazon.com/free/  

#### Try Next: Use free Google GPU for deep learning.  
    Setup environment with tensorflow, kearas using Ubuntu machine.  
...  
---  

### May 11-12, 2020 Setup environment: dlpy  

  * Finished setting up conda environment on Ubuntu side, "dlpy" 
  * tensorflow 2.2, keras, tensorboard included.  
  * jupyter notebook, numpy, pandas, matplotlib, scipy, scikit-learn, blas included.   
  * Some packages need pip, some need to specify channel conda-forge.  
  * Also per book, HDF5, Graphviz, opencv.  
  * Q) tensorflow-datasets?  nmist_fashion example on tensorflow doc site.  
  
