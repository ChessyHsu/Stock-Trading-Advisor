from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.notes import Notes
from app.schemas.notes import Note, NoteIn


class CRUDItem(CRUDBase[Notes, Note, NoteIn]):
    def create_note(
        self, db: Session, *, obj_in: NoteIn) -> Notes:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_notes(
        self, db: Session) -> List[Notes]:
        cur = db.execute('''SELECT * FROM notes''')
        return (
            cur.all()
        )


notes = CRUDItem(Notes)