from fastapi import APIRouter
from persistence.database import database as db
from pydantic import BaseModel
import sqlalchemy
from typing import List


router = APIRouter(tags=['Screeners'])

metadata = sqlalchemy.MetaData()
notes = sqlalchemy.Table(
    "notes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("text", sqlalchemy.String),
    sqlalchemy.Column("completed", sqlalchemy.Boolean),
)
# metadata.create_all(engine)

class NoteIn(BaseModel):
    text: str
    completed: bool


class Note(BaseModel):
    id: int
    text: str
    completed: bool


@router.get("/notes/", response_model=List[Note])
async def read_notes():
    query = notes.select()
    return await db.fetch_all(query)


@router.post("/notes/", response_model=Note)
async def create_note(note: NoteIn):
    query = notes.insert().values(text=note.text, completed=note.completed)
    last_record_id = await db.execute(query)
    return {**note.dict(), "id": last_record_id}

# @router.get("/prices/", response_model=List[Price])
# async def read_prices():
#     query = prices.select()
#     return await db.fetch_all(query)