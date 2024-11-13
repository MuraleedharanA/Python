import pandas as pd

df = pd.read_csv(r"C:\Users\Administrator\Desktop\UST_Training\DAY13\titanic.csv")

#Calculate the survival rate by gender.(how many peope survived per gender)
#print(df.head())

grpGndr=(df.groupby(['Sex']).agg({'Survived':sum})/100).reset_index
print(grpGndr)