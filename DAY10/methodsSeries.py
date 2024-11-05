#impl any 5 methods in a series and any 5 attributes in a series

import pandas as pd

series1=pd.Series([1,2,3,4])
series2=pd.Series([5,5,6,7])

print("Is Series 1 Unique? ",series1.is_unique)
print("Is Series 2 Unique? ",series2.is_unique)

print("Sum of series1 and series2 : \n",series1.add(series2))
print("Difference of series1 and series2 :\n",series1.subtract(series2))

print("abs Difference of series1 and series2 :\n",series1.subtract(series2).abs())

print("Head 2 of series1 : \n",series1.head(1))
print("Tail 2 of series2 : \n",series2.tail(2))

