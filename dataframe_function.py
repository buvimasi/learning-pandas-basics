import pandas as pd
import numpy as np
 
# Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
df = pd.DataFrame(d)
print ("The transpose of the data series is:")
print(df.T)
print ("Row axis labels and column axis labels are:")
print(df.axes)
print ("The data types of each column are:")
print(df.dtypes)
print ("Is the object empty?")
print(df.empty)
print ("The dimension of the object is:")
print(df.ndim)
print ("The shape of the object is:")
print(df.shape)
print ("The total number of elements in our object is:")
print(df.size)
print ("The total number of elements in our object is:")
print(df.size)
print ("The first two rows of the data frame is:")
print(df.head(2))
print ("The last two rows of the data frame is:")
print(df.tail(2))
print("sum of dataframe")
print(df.sum())
print(df.mean())
#summarizing data
print(df.describe())
print(df.describe(include=['object']))
print(df.describe(include='all'))
