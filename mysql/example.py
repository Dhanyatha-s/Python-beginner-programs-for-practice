import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
  #database="example"
)

mycursor=mydb.cursor()
mycursor.execute("create database mydata")


