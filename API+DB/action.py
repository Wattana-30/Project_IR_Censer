from DB import gat_data as c

class Action:
    def selectWH(ID):
        data = c.selectWH(ID)
        return data
    
    def insertWH(address,name,last_name):
        data = c.insertWH(address,name,last_name)
        return data