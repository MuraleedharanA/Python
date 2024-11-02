import pandas as pd

data={
    'Name':['a','v','b'],
    'Age':[34,45,67],
    'Place':['BLR','CHN','HYD']
}
df = pd.DataFrame(data)
print(df)