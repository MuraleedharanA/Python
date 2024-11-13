import pandas as pd
import numpy as np
"""Concat 2 dataframes"""
df1=pd.DataFrame({
    'Name' : ['A','B','C'],
    'Age' : [20,30,40],
    'Place' : ['A','C',np.nan]
})

#print(df1)

df2=pd.DataFrame({
    'Name' : ['A2','B2','C2'],
    'Age' : [20,30,40],
    'Place' : ['A','B',np.nan]
})

df3=pd.concat([df1,df2],ignore_index=True)
#change city at index 2 to mumbai
#df3.loc[2,'Place']="Mumbai"

#change city at B to mumbai

#df3.loc[df3['Name']=='B','Place']='mumbai'
#print(df3)

#fill with NA
df4=df3.fillna("Mumbai")

print(df4['Place'].value_counts())

