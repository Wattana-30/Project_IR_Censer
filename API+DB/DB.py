import mysql.connector


def con():
    mydb = mysql.connector.connect(
        host="localhost",
        user="project_ir_censer",
        password="123456",
        database="project_ir_censer"
    )
    return mydb


class gat_data:
    def selectWH(ID):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM ir_censer WHERE id = {}".format(ID)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        return data

    def insertWH(address, name, last_name):
        mydb = con()
        mycursor = mydb.cursor()
        sql = "INSERT INTO ir_censer(address,name,last_name)VALUES('{}','{}','{}')".format(
            address, name, last_name)
        mycursor.execute(sql)
        mydb.commit()
        data = mycursor.fetchall()
        return data

    def updateHW(status,ID):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "UPDATE ir_censer SET status= '{}' WHERE id = '{}'".format(status,ID)
        mycursor.execute(sql)
        mydb.commit()
        return True

    def deleteHW(ID):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "DELETE FROM ir_censer WHERE id='{}'".format(ID)
        mycursor.execute(sql)
        mydb.commit()
        ID = mycursor.lastrowid
        return ID
