import mysql.connector as MyConn

mydb = MyConn.connect(host="localhost", user="root", password="root", database="pythondb")
db_cursor = mydb.cursor()

db_DeleteByRoll="DELETE FROM emp WHERE Roll=10"
db_cursor.execute(db_DeleteByRoll)  
print("Deleted Successfully")

db_cursor.close()
mydb.close()