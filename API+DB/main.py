from typing import Union
from action import Action as a
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/get")
def selectWH(ID):
    data = a.selectWH(ID)
    return data

@app.get("/get_in")
def insertWH(address,name,last_name):
    data = a.insertWH(address,name,last_name)
    return data

@app.get("/get_update")
def updateHW(status,ID):
    data = a.updateHW(status,ID)
    return data

@app.get("/get_delete")
def deleteHW(ID):
    data = a.deleteHW(ID)
    return data


if __name__  == "__main__":
    uvicorn.run(app, host="192.168.216.103",port=8080)