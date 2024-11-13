import sqlite3

connection = sqlite3.connect(r"C:\Users\Administrator\Desktop\UST_Training\DAY15_SQL_Learning\Chinook_Sqlite.sqlite")
cursor = connection.cursor()

cursor.execute(
   """UPDATE Customer 
   SET Email=?
   WHERE CustomerId=?""",('athira.gmail.com',679)
)
connection.commit()
cursor.execute(
   """ SELECT * FROM Customer WHERE CustomerId=679"""
)
rows=cursor.fetchall()
desc =cursor.description
cols = [col[0] for col in desc]
#rows=cursor.fetchall()
print(rows)
print(cols)