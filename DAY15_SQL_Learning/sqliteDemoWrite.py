import sqlite3

connection = sqlite3.connect(r"C:\Users\Administrator\Desktop\UST_Training\DAY15_SQL_Learning\Chinook_Sqlite.sqlite")
cursor = connection.cursor()

new_customer = (6799,'Athira','Muraleedharan','ABC','A@gmail.com','IND')
cursor.execute(
    """
    INSERT INTO Customer(CustomerID, FirstName, LastName, Company, Email, Country) VALUES(?,?,?,?,?,?)
    """,new_customer
)

connection.commit()
print("New cust added")