import pandas as pd
#1.create a pivot table showing the total sales per store
#2.total sales per region

datatest={
    'Store':['Store1','Store1','Store2','Store2','Store3','Store3','Store4','Store5'],
    'Region':['North','North','South','South','East','East','North','South'],
    'Sales':[200,150,300,250,400,350,400,500]
}
df=pd.DataFrame(datatest)
#print(df)
print("\n",df.groupby(['Store']).agg({'Sales':sum}).reset_index())

df3=df.groupby(['Region']).agg({'Sales':sum}).reset_index()
df4=pd.merge(df,df3,on='Region',how='left',suffixes=['_store','_salesRegion'])
df4['RegionSales_Percentage'] = df.groupby(['Store']).agg({'Sales':sum})/df4['Sales_salesRegion']
print(df4)
