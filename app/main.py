from typing import List

import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel
from config import DBconfig

# # SQLAlchemy specific code, as with any other app
# DATABASE_URL = "sqlite:///./test.db"
# DATABASE_URL = "postgresql://epzqbkmaqhhbos:d74313ac4560b18b6a0f2a5969ece5f39e231762b06c94db7f344b91ed3d54aa@ec2-184-73-243-101.compute-1.amazonaws.com:5432/db641vr50biusv"
DATABASE_URL = f"postgresql://{DBconfig.username}:{DBconfig.password}@{DBconfig.host}/postgres"
database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

notes = sqlalchemy.Table(
    "notes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("text", sqlalchemy.String),
    sqlalchemy.Column("completed", sqlalchemy.Boolean),
)


engine = sqlalchemy.create_engine(
    DATABASE_URL# , connect_args={"check_same_thread": False}
)
metadata.create_all(engine)


class NoteIn(BaseModel):
    text: str
    completed: bool


class Note(BaseModel):
    id: int
    text: str
    completed: bool


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/notes/", response_model=List[Note])
async def read_notes():
    query = notes.select()
    return await database.fetch_all(query)


@app.post("/notes/", response_model=Note)
async def create_note(note: NoteIn):
    query = notes.insert().values(text=note.text, completed=note.completed)
    last_record_id = await database.execute(query)
    return {**note.dict(), "id": last_record_id}

@app.get("/")
def hello():
    return {"message":"Hello Chessy.com !!"}
