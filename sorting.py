import pandas as pd
import numpy as np

un_sorted=pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],colu
mns=['col2','col1'])
print(unsorted)
#by label
sorted=un_sorted.sort_index()
print(sorted)
#by axis=1
sorted=un_sorted.sort_index(axis=1)
print(sorted)
#sort descending order
sorted=un_sorted.sort_index(ascending=False)
#by value
sorted=un_sorted.sort_values(by='col1')
#sorting algorithm
sorted=un_sorted.sort_values(by='col1',kind='mergesort')
