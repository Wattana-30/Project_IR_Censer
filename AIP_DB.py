import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="logtast",
  password="logtast",
  database="logtast"
)

print(mydb)