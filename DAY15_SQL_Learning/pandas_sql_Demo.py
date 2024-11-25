import sqlite3
import pandas as pd

connection = sqlite3.connect(r"C:\Users\Administrator\Desktop\UST_Training\DAY15_SQL_Learning\Chinook_Sqlite.sqlite")
cursor = connection.cursor()



query = """ SELECT * FROM Customer limit 100"""

df=pd.read_sql_query(query,connection)
print(df.head())

connection.close()