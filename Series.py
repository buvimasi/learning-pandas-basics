#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print(s)
#series with index
data1 = np.array(['a','b','c','d'])
s1 = pd.Series(data,index=[100,101,102,103])
print(s1)
#series created using dict
data2 = {'a' : 0., 'b' : 1., 'c' : 2.}
s2= pd.Series(data)
print(s2)
#Series created using Scalar
s3 = pd.Series(5, index=[0, 1, 2, 3])
print(s3)
#retrieve the first element
print(s1[0])
#retrieve the first three element
print(s1[:3])

