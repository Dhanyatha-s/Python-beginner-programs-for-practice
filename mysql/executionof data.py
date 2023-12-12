import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="example"
)
mycursor=mydb.cursor()
sql="select * from customers"
mycursor.execute(sql)
row=mycursor.fetchall()
for i in row:
    print("name:",i[0],"Address:",i[1])
