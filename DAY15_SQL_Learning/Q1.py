import sqlite3
import pandas as pd

"""determine sales total for each country in inv table"""

connection = sqlite3.connect(r"C:\Users\Administrator\Desktop\UST_Training\DAY15_SQL_Learning\Chinook_Sqlite.sqlite")
cursor = connection.cursor()

query = """ SELECT BillingCountry,sum(Total) as Total_Sales FROM Invoice GROUP BY BillingCountry"""

df=pd.read_sql_query(query,connection)
print(df)

connection.close()