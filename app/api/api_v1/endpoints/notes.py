from typing import Any, List
from app.schemas import notes

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.Note])
def read_notes(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve notes.
    """
    notes = crud.notes.get_notes(db=db)
    # notes = crud.notes.get_multi(db=db)
    return notes


@router.post("/", response_model=schemas.Note)
def create_note(
    *,
    db: Session = Depends(deps.get_db),
    item_in: schemas.NoteIn,
) -> Any:
    """
    Create new item.
    """
    note = crud.notes.create(db=db, obj_in=item_in)
    return note