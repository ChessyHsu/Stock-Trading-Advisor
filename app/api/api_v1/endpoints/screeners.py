from typing import Any, List
from datetime import date
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.Price])
def read_prices_by_date(
    db: Session = Depends(deps.get_db),
    date: date = date(2021, 8, 9),
    sortby: str = "volume",
    order: str = "DESC"
) -> Any:
    """
    Retrieve prices.
    """
    prices = crud.prices.get_company_prices_by_date(db=db, date=date, sortby=sortby, order=order)
    return prices
