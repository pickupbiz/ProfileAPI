from fastapi import APIRouter
from pydantic import BaseModel

router= APIRouter()

class Address(BaseModel):
    name: str
    line1: str
    line2: str
    city: str
    pin: int

@router.get("/contact")
def getContact():
    return "Contact Information"

@router.post("/contact/address")
def getaddress(address: Address):
    return {"address": f"{address.name}, {address.line1}, {address.line2}, {address.city}-{address.pin}"}