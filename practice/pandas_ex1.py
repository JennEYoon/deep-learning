# Simple Pandas code review, practice  
### Feb 5, 2023 Sunday 5:40 pm  
### Jennifer E Yoon author  

import pandas as pd 
from pandas import Series, DataFrame

# index as immutable array, p 106 VanderPlas 2017  
ind = pd.Index([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  
print(ind, type(ind))

print(ind[2])   # ith item
print(ind[-1])  # last item
print(ind[::3])  # repeat every 3rd starting at 0th.  

### reversed repeat
print(ind[2::-1])  # reversed repeat, count from -2 not 0. [8, 7, 6, ...] I thinkt this is correct.  
          # or it could be reversed from 2 to 10, [10, 9, 8, .. 3, 2]
print(ind[::-1])  # this reverses the whole thing starting from last item.   
          # so likely count backwards, starting from last as 0th.  
# >>> Wrong! [2, 1, 0].  Start from ith, the reverse by step one repeatedly.  
print(ind[8::-2])   # expect [8, 6, 4, 2, 0]  Start from ith, reverse by step -n, repeat. 
          
### [i::+/-n]  Start from ith from left, then repeat (2nd :) every nth, or -nth.  
print(ind[0::-2])  # only gives "[0]"  
# so [::-1] must be a special case. if 0th is not specified, start from last.  
print(ind[::-2])  # in reverse, not specified start is same as start from last  
print(ind[-1::-2])  # count from right assumed in reverse flow, if omitted.  