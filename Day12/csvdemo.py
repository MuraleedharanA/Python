import pandas as pd
import numpy as np
"""Merge 2 dataframes"""
df1=pd.DataFrame({
    'Name' : ['A','B','C','d'],
    'Age' : [20,30,40,30],
    'Place' : ['A','C','abc','bvc']
})


df2=pd.DataFrame({
    'Name' : ['A','B','C'],
    'Salary' : [20,30,40],
    'Work_Place' : ['A','B','jg']
})

df3=pd.merge(df1,df2,on='Name',how='left',suffixes=["_df1","_df2"])
df3.to_csv("samplecsv.csv",index=False)