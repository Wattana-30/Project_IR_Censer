from typing import Union
from action import Action as a
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/get")
def selectHW(ID):
    data = a.selectHW(ID)
    return data

@app.get("/get_insert")   
def insertHW(address,name,last_name):
    data = a.insertHW(address,name,last_name)
    return data

@app.get("/get_update")
def updateHW(status,ID):
    data = a.updateHW(status,ID)
    return data

@app.get("/get_delete")
def deleteHW(ID):
    data = a.deleteHW(ID)
    return data

@app.get ("/get_select_all")
def selectHW_All():
    data = a.selectHW_All()
    return data


if __name__  == "__main__":
    uvicorn.run(app, host="192.168.216.103",port=80)