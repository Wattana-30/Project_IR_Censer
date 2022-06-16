import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="project_ir_censer,
  password="123456",
  database="project_ir_censer"
)

print(mydb)