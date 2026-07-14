from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()

class ProjectCategory(BaseModel):
    catId : int
    catName : str

@router.get("/pro")
def getProject():
    return "This is my Project"

@router.post("/pro/addcat")
def addCat(projectCategory: ProjectCategory):
    return {"Project Category ID ": projectCategory.catName}
