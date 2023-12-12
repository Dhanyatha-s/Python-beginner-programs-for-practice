
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="example"
)
mycursor=mydb.cursor()
#mycursor.execute("create table customers(name varchar(20),address varchar(20))")
sql="insert into customers(name,address) values(%s,%s)"
val=("anna","Highway 11")
#sql="INSERT INTO `customers`(`name`, `address`) VALUES ('Anna','Belgium')"
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"record inserted.")
#sql="select * from customers"
#print(mydb)
