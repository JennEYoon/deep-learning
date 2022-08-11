# Chapter 1 notes, nnfs  

Math and Python code for neural network forward pass, 3 layers example.  

#### A math representation of 3-layer forward pass, with several nodes per layer.  
<img src="./images/c1_forward_pass_math.png" width='700' alt='math image'>  

#### Corresponding Python code  
Nested math operations, each layer is summed across number of nodes in the layer.    
<img src="./images/c1forward_pass_python.png" width='700' alt='code image'>  

NumPy functions used:  

np.T -- transpose
np.dot -- matrix dot product  
np.log -- natural log  
np.exp -- math e (anti-log)   