import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(4))
print(s)
#Returns the list of the labels of the series
print ("The axes are:")
print(s.axes)
#Returns True if series is empty
print(s.empty)
#Returns the number of dimensions of the object
print(s.ndim)
#Returns the size(length) of the series
print(s.size)
#Returns the actual data in the series as an array
print(s.values)
#returns the first n rows
print(s.head(2))
#returns the last n rows
print(s.tail(2))
