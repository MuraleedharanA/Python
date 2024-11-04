import pandas as pd


series1=pd.Series([23,12,34],index=["Athira","Syam","Gopi"])
print(series1)
print("Mark of 3rd Person :",series1.iloc[2])
print("Mark of Athira : ",series1.loc["Athira"])
print(series1[series1>30])