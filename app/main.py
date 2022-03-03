from fastapi import FastAPI

from app.db.init_db import init_db
from app.db.session import SessionLocal

from app.core.config import settings
from app.api.api_v1.api import api_router

# # SQLAlchemy specific code, as with any other app
# DATABASE_URL = "sqlite:///./test.db"
# DATABASE_URL = "postgresql://epzqbkmaqhhbos:d74313ac4560b18b6a0f2a5969ece5f39e231762b06c94db7f344b91ed3d54aa@ec2-184-73-243-101.compute-1.amazonaws.com:5432/db641vr50biusv"

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    # Initialize db
    db = SessionLocal()
    init_db(db)

    
@app.get("/")
def hello():
    return {"message":"Hello Chessy.com !!"}

app.include_router(api_router, prefix=settings.API_V1_STR)