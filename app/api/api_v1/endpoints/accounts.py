from typing import Any, List
from fastapi import APIRouter, Body, Depends, HTTPException
from app import crud, models, schemas
from app.api import deps

from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/signup")
async def sign_up(
    *,
    db: Session = Depends(deps.get_db),
    username: str = Body(...),
    password: str = Body(...),
    ) -> Any:
    account = crud.account.get_by_username(db, username=username)
    if account:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
        
    account_in = schemas.AccountCreate(username=username, password=password)
    print(account_in)
    account = crud.account.create(db, obj_in=account_in)
    return account

@router.get("/me", response_model=schemas.Account)
def read_user_me(
    db: Session = Depends(deps.get_db),
    current_user: models.Account = Depends(deps.get_current_account),
) -> Any:
    """
    Get current user.
    """
    return current_user