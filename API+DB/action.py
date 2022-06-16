from DB import gat_data as c

class Action:
    def selectWH(ID):
        data = c.selectWH(ID)
        return data
    
    def insertWH(address,name,last_name):
        data = c.insertWH(address,name,last_name)
        return data

    def updateHW(status,ID):
        t = c.updateHW(status,ID)
        if(t == True):
            data = c.selectWH(ID)
        else:
            data = {"ERROR":True}
        return data


    def deleteHW(ID):
        data = c.deleteHW(ID)
        return data 

    