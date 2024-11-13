import pandas as pd

df = pd.read_csv(r"C:\Users\Administrator\Desktop\UST_Training\DAY13\titanic.csv")

#create col family size. calculate avg survival rate by family size. merge the family survival rate back to original df. display resulting df
#print(df.head())

df['Family Size']=df['SibSp']+df['Parch']
#print(df.head())

avgSurvivalRate = (df.groupby(['Family Size']).agg({'Survived':sum})/100).reset_index()
#print(avgSurvivalRate)
avgSurvivalRate.columns=['Family Size','Family Survival Rate']
newDf=pd.merge(df,avgSurvivalRate,on='Family Size')
print(newDf.head())
newDf.to_csv('filtered.csv')