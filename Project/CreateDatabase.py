import mysql.connector as MyConn

mydb=MyConn.connect(host="localhost",user = "root",password ="root")
db_cursor=mydb.cursor()

db_cursor.execute("Create database pythondb")

print ("Database Created Successfully..!")