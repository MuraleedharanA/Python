import pandas as pd

dict={
    'num1':[1,2,3],
    'num2':[4,5,6],
    'num3':[7,8,9]
}
df1=pd.DataFrame(dict)

print(df1.mean(axis=1))