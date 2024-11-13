import sqlite3
import pandas as pd

"""determine sales total for each country in inv table using pandas
write result to SQL table
"""

connection = sqlite3.connect(r"C:\Users\Administrator\Desktop\UST_Training\DAY15_SQL_Learning\Chinook_Sqlite.sqlite")
cursor = connection.cursor()

query = """ SELECT * FROM Invoice """

df=pd.read_sql_query(query,connection)
#print(df.head())
#grpGndr=(df.groupby(['Sex']).agg({'Survived':sum})/100).reset_index
dfgrp=df.groupby('BillingCountry')['Total'].sum().reset_index()
print(dfgrp)

#write to sql table
dfgrp.to_sql('summary_sales_by_country',connection,if_exists='replace',index=False)

connection.close()