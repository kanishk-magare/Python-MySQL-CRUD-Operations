import mysql.connector as MyConn

mydb = MyConn.connect(host="localhost", user="root", password="root", database="pythondb")
db_cursor = mydb.cursor()

try:
    sql = "INSERT INTO Emp (Roll, Ename) VALUES (%s, %s)"
    val = (10, "kanishk")
    db_cursor.execute(sql, val)
    mydb.commit()  # Commit the changes to the database
    print(db_cursor.rowcount, "Record Inserted...!")
except MyConn.Error as err:
    print(f"Error inserting record: {err}")
finally:
    db_cursor.close()
    mydb.close()
