from cgitb import reset
from fastapi import FastAPI


app = FastAPI()


@app.on_event("startup")
async def startup():
    from persistence.database import database
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    from persistence.database import database
    await database.disconnect()


@app.get("/")
def hello():
    return {"message":"Hello Chessy.com !!"}


from api import register_routers
register_routers(app)