import pandas as pd

df = pd.read_csv(r"C:\Users\Administrator\Desktop\UST_Training\Titanic\titanic.csv")
#print(df.head())

#select only age column and print first 5 rows

#print((df.loc[:,"Age"]).head())

#create subset of dataframe with 2 columns 'age','sex'.print 5 rows.(not loc or iloc)

#print(df[["Sex","Age"]].head)

#filter out all the people whos age is <25

#print(df[df['Age']>25])

#length of data

#print(len(df.index))

#avg age of all people 

#print(df['Age'].mean())

#get the avg fare price of all the male pass whose age is <25

ageDf=df[df['Age']<25]
maledf=ageDf[ageDf['Sex']=='male']
avg = maledf['Fare'].mean()
#print(avg)
df_final=(df[(df['Sex']=='male') & (df['Age']<25)])
#print(df_final['Fare'].mean())
df_final.to_csv("filtered.csv",index=False)

#what % of pass survived the titanic

print((len(df[df['Survived']==1].index)/(len(df.index)))*100)

