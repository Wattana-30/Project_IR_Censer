from DB import gat_data as c

class Action:
    def selectHW(ID):
        data = c.selectHW(ID)
        return data
    
    def insertHW(address,name,last_name):
        data = c.insertHW(address,name,last_name)
        return data

    def updateHW(status,ID):
        t = c.updateHW(status,ID)
        if(t == True):
            data = c.selectHW(ID)
        else:
            data = {"ERROR":True}
        return data


    def deleteHW(ID):
        data = c.deleteHW(ID)
        return data 


    def selectHW_All():
        data = c.selectHW_All()
        return data
    