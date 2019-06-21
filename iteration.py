import pandas as pd
import numpy as np
 
N=10
df = pd.DataFrame({
   'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
   'B': np.linspace(0,stop=N-1,num=N),
   'C': np.random.rand(N),
   'D': np.random.choice(['Low','Medium','High'],N).tolist(),
   'E': np.random.normal(100, 10, size=(N)).tolist()
   })

for col in df:
   print col
#iteritems()
df = pd.DataFrame(np.random.randn(4,3),columns=['col1','col2','col3'])
for key,value in df.iteritems():
   print key,value
#iterrows()
for row_index,row in df.iterrows():
   print row_index,row
#itertuples()
for row in df.itertuples():
    print row
