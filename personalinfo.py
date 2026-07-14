from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class FullName(BaseModel):
    fname: str
    lname: str

class LongName(BaseModel):
    fname: str
    mname: str
    lname: str

@router.get("/pi")
def getPI():
    return "Personal Information..."

@router.post("/pi/fullname")
def getFullName(fullname: FullName):
    return {"fullname" : fullname.fname + " " + fullname.lname}

@router.post("/pi/longname")
def getLongName(longname: LongName):
    return {"longname": longname.fname + " " + longname.mname + " " + longname.lname}