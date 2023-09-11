import mysql.connector as MyConn

mydb = MyConn.connect(host="localhost", user="root", password="root", database="pythondb")
db_cursor = mydb.cursor()


try:
    db_updatedata="UPDATE emp set roll=%s WHERE Ename=%s"
    db_value=(40,"Shiva")
    db_cursor.execute(db_updatedata,db_value)  
    print("Updated Successfully")
except MyConn.Error as err:
    print("Error updating" , err)
finally:
    db_cursor.close()
    mydb.close()