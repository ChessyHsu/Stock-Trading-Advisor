from pydantic import BaseModel

class Note(BaseModel):
    id: int
    text: str
    completed: bool
    
    class Config:
        orm_mode = True
        

class NoteIn(Note):
    text: str
    completed: bool