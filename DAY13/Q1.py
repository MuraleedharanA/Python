import pandas as pd

df = pd.read_csv(r"C:\Users\Administrator\Desktop\UST_Training\DAY13\titanic.csv")

#Compare the avg age of pass who survived with passengers who didnt

#print(df.head())
#avg age of pass who survived

survivedDF=df[df['Survived']==1]
avgage=survivedDF['Age'].mean()
print(avgage)

notsurvivedDF=df[df['Survived']==0]
avgageofnot=notsurvivedDF['Age'].mean()
print(avgageofnot)