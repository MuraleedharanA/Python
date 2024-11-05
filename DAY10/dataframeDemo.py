import pandas as pd

name=pd.Series(["athi","syam"])
team=pd.Series(["IT","Ops"])
dic={"Name":name, "Team":team}
df=pd.DataFrame(dic)
print(df)

for row_index,row_val in df.iterrows():
    print("------------------------")
    print("Row index :",row_index)
    print("Row Value :",row_val)


for col_name,col_val in df.iteritems():
    print("------------------------")
    print("Col NAme :",col_name)
    print("Col Value :",col_val)