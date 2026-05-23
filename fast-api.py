from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi import HTTPException

app = FastAPI()

class Tea(BaseModel):
    id:int
    name:str
    origin:str

# Since we don't have any DB as of now
teas : List[Tea] = []

# Decorators - In order to setup routing and request methods
@app.get("/")
def readRoot():
    return{"message" : "Welcome to Chai Code"}

@app.get("/teas")
def getTeas():
    return teas

@app.post("/teas")
def addTea(newTea:Tea):
    teas.append(newTea)
    return newTea

@app.put("/teas/{teaId}")
def updateTea(teaId:int, updatedTea:Tea):
    for index, tea in enumerate(teas):
        if tea.id == teaId:
            teas[index] = updatedTea
            return updatedTea
    # This is incase the loop did not find the matching Tea id
    raise HTTPException(status_code = 404, detail="Tea not found")
@app.delete("/teas/{teaId}")
def deleteTea(teaId:int):
    for index,tea in enumerate(teas):
        if tea.id == teaId:
            deleted = teas.pop(index)
            return{
                "message": "Following tea has been successfully deleted",
                "deletedTea": deleted
            }
    # This is incase the loop did not find the matching Tea id
    raise HTTPException(status_code=404, detail="Tea not found")