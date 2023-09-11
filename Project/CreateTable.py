import mysql.connector as MyConn

mydb = MyConn.connect(host="localhost", user="root", password="root", database="pythondb")
db_cursor = mydb.cursor()

try:
    db_cursor.execute("CREATE TABLE IF NOT EXISTS Emp (Roll INT , Ename VARCHAR(25))")
    print("Table created sucessfully..!")
except MyConn.Error as err:
    print("Error creating table: {err}")
finally:
    db_cursor.close()
    mydb.close()
