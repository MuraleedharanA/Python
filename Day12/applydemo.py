import pandas as pd
import numpy as np


"""Apply """
df1=pd.DataFrame({
    'Name' : ['A','B','C'],
    'Age' : [20,30,40],
    'Place' : ['A','C','abc']
})


df2=pd.DataFrame({
    'Name' : ['A','B','C'],
    'Salary' : [20,30,40],
    'Work_Place' : ['A','B','jg']
})

def isevenNum(val):
    if val%2==0:
        return 'even'
    else:
        return 'odd'
    

df3=pd.merge(df1,df2,on='Name',how='left',suffixes=["_df1","_df2"])
df3['Is Even']=""
df3['Is Even']=df3['Salary'].apply(isevenNum)
print(df3)
