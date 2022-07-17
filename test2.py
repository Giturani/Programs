import mysql.connector as con
mydb = con.connect(host = "localhost" , user = "root" , passwd = "root")
cursor1 = mydb.cursor()
cursor1.execute("insert into gitanjali.ineuron values(101 , 'abcdef' , 'xyz@gmail.com' , 100 , 30)")
mydb.commit()