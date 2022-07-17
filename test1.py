import mysql.connector as con
mydb = con.connect(host = "localhost" , user = "root" , passwd = "root")
cursor1 = mydb.cursor()
#cursor1.execute("create database Gitanjali")

#s = "CREATE TABLE GITANJALI.INEURON(emp_id int(10) , emp_name varchar(80) , emp_mailid varchar(20) , emp_salary int(6) , emp_attendace int(3))"
#q1 = cursor1.execute(s)
q2 = cursor1.execute("select * from gitanjali.ineuron")
print(q2)
