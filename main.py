from fastapi import FastAPI
from personalinfo import router as pi_router
from contactinfo import router as contact_router
from mathinfo import router as math_router
from projectinfo import router as pro_router

app= FastAPI()
app.include_router(pi_router)
app.include_router(contact_router)
app.include_router(math_router)
app.include_router(pro_router)

@app.get("/")
def getRoot():
    return "Profile API is up and running..."