from pydantic import BaseModel
from typing import Optional

class Note(BaseModel):
    id: Optional[int] = None
    text: str
    completed: bool
    
    class Config:
        orm_mode = True
        

class NoteIn(Note):
    text: str
    completed: bool