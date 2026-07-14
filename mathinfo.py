from fastapi import APIRouter
from pydantic import BaseModel

router= APIRouter()

class TwoNum(BaseModel):
    num1: int
    num2:int

@router.get("/mi")
def getMath():
    return "Math with Fun"

@router.post("/mi/sum")
def getSum(sum: TwoNum):
    return {"result": sum.num1 + sum.num2}

@router.post("/mi/pow")
def getPow(p: TwoNum):
    return {"result": p.num1** p.num2}
