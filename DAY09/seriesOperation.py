import pandas as pd


series1=pd.Series([1,2,3],index=[1,2,3])
series2=pd.Series([4,5,6],index=[1,2,4])
print(series1+series2)
print(series1*series2)

print(series1.add(series2,fill_value=0))