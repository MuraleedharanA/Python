import pandas as pd
import numpy as np

arr=np.array([10,15,45,89])
d={"name":"athira","Age":"32"}
#s=pd.Series(arr,index=['a','b','c','d'])
#s=pd.Series(50,index=['a','b','c','d'])
s=pd.Series(d)
print(s['name'])