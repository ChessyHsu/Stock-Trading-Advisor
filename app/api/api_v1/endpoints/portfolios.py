from typing import Any, List
from app.models import portfolio
from app.schemas import notes
from datetime import date
from fastapi import APIRouter, Body, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.Portfolio])
def get_user_portfolios(
    db: Session = Depends(deps.get_db),
    current_account: models.Account = Depends(deps.get_current_account)
):
    if not current_account:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication not passed",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return current_account.portfolios

@router.post("/", response_model=schemas.Portfolio)
def create_portfolio(*,
    db: Session = Depends(deps.get_db),
    item_in: schemas.PortfolioCreate,
) -> Any:
    """
    Create new portfolio.
    """
    account = crud.account.get(db, id=item_in.ownerId)
    if not account:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The account with the id is not exists in the system.",
        )
        
    portfolio_in = schemas.PortfolioCreate(
                        ownerId=item_in.ownerId,
                        portfolioName=item_in.portfolioName,
                    )
    
    print(portfolio_in)
    portfolio = crud.portfolio.create(db, obj_in=portfolio_in)
    return portfolio


@router.get("/{portfolio_id}", response_model=schemas.PortfolioWithStocks)
def get_portfolio_detail(
    portfolio_id: int,
    db: Session = Depends(deps.get_db),
    current_account: models.Account = Depends(deps.get_current_account)
):

    portfolio = crud.portfolio.get(db, id=portfolio_id)
    if not portfolio:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Portfolio not found"
        )
    
    return portfolio

@router.put("/{portfolio_id}", response_model=schemas.PortfolioWithStocks)
def update_portfolio(
    *,
    db: Session = Depends(deps.get_db),
    portfolio_id: int,
    update_symbol: str = Body(...),
    update_operation: str = Body(...),
    current_account: models.Account = Depends(deps.get_current_account),
) -> Any:
    """
    Update stock in portfolio.
    """
        
    portfolio = crud.portfolio.get(db, id=portfolio_id)
    if not portfolio:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Portfolio not found"
        )
    if portfolio.ownerId != current_account.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Not enough permissions"
        )
        
    if update_operation == "add":
        # Check if add duplicate stock in portfolio
        for stock in portfolio.stocks:
            if stock.stockSymbol == update_symbol:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="The stock is already in this portfolio"
                )
        item = crud.portfolio.add_stock(db=db, portfolio=portfolio, symbol=update_symbol)
    elif update_operation == "remove":
        item = crud.portfolio.remove_stock_by_symbol(db=db, portfolio=portfolio, symbol=update_symbol)
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Operation not support"
        )
        
    if not item:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Operation failed when update DB"
        )
    
    return item

@router.put("/{portfolio_id}/clean", response_model=schemas.PortfolioWithStocks)
def clean_portfolio(
    *,
    db: Session = Depends(deps.get_db),
    portfolio_id: int,
    current_account: models.Account = Depends(deps.get_current_account),
) -> Any:
    """
    Clean all stocks in a portfolio.
    """
        
    portfolio = crud.portfolio.get(db, id=portfolio_id)
    if not portfolio:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Portfolio not found"
        )
    if portfolio.ownerId != current_account.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Not enough permissions"
        )
        
    item = crud.portfolio.clean_all(db=db, portfolio=portfolio)
    
    if not item:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Operation failed when update DB"
        )
    
    return item