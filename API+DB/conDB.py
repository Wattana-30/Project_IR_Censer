
from unicodedata import name
import mysql.connector
def con():
    mydb = mysql.connector.connect(
        host="localhost",
        user="logtast",
        password="logtast",
        database="logtast"
        )
    return mydb
class GetData:
    def selectHW():    
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql ="SELECT * FROM `hard_ware`"
        mycursor.execute(sql)
        data = mycursor.fetchall()
        return data
    def insertWH():
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql ="INSERT INTO hard_ware (name,hw_name,status,value)VALUES('B4','pump','OFF','0.00')"
        mycursor.execute(sql)
        mydb.commit()
        ID = mycursor.lastrowid
        return ID
    def updateHW():
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql ="UPDATE hard_ware SET status= 'ON' WHERE id = '25'"
        mycursor.execute(sql)
        mydb.commit()
        ID = mycursor.lastrowid
        return ID
    def deleteHW():
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql ="DELETE FROM hard_ware WHERE id='25'"
        mycursor.execute(sql)
        mydb.commit()
        ID = mycursor.lastrowid
        return ID
    
    def deleteMin():
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql ="DELETE FROM 'hard_ware' WHERE id = (SELECT MIN(id) FROM hard_ware )"
        mycursor.execute(sql)
        mydb.commit()
        ID = mycursor.lastrowid
        return ID
            
    
ID = GetData.deleteMin()
print(ID)
    
    
    
    