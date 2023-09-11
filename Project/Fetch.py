import mysql.connector as MyConn

mydb = MyConn.connect(host="localhost", user="root", password="root", database="pythondb")
db_cursor = mydb.cursor()

try:
    db_cursor.execute("SELECT * FROM pythondb.emp")
    # db_select=db_cursor.fetchone()
    db_select=db_cursor.fetchall()

    print(db_select)
except MyConn.Error as err:
    print("Error Fetching", err)
finally:
    db_cursor.close()
    mydb.close()
