import pandas as pd
import numpy as np

unsorted=pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],colu
mns=['col2','col1'])
print(unsorted)
#by label
sorted=unsorted.sort_index()
print(sorted)
#by axis=1
sorted=unsorted.sort_index(axis=1)
print(sorted)
#sort descending order
sorted=unsorted.sort_index(ascending=False)
#by value
sorted=unsorted.sort_values(by='col1')
#sorting algorithm
sorted=unsorted.sort_values(by='col1',kind='mergesort')
