#import the pandas library and aliasing as pd
import pandas as pd
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)
#insert column name
data1 = [['Alex',10],['Bob',12],['Clarke',13]]
df1 = pd.DataFrame(data,columns=['Name','Age'])
print(df1)
#created from dict ndarray
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print(df)
#with row and column index
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]

#With two column indices, values same as dictionary keys
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])

#With two column indices with one index with other name
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
print(df1)
print(df2)
#created dict of series
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df)
#column selection
print(df ['one'])
# Adding a new column to an existing DataFrame object with column label by passing new series

print ("Adding a new column by passing as Series:")
df['three']=pd.Series([10,20,30],index=['a','b','c'])
print(df)

print ("Adding a new column using the existing columns in DataFrame:")
df['four']=df['one']+df['three']

print(df)
# using del function
print ("Deleting the first column using DEL function:")
del df['one']
print(df)
# using pop function
print ("Deleting another column using POP function:")
df.pop('two')
print(df)
