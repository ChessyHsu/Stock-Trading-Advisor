from fastapi import APIRouter

router = APIRouter()


@router.get("/{username}")
async def get_user_portfolios(username: str):
    return {"username": "fakecurrentuser"}


@router.get("/{portfolio_id}")
async def get_portfolio(portfolio_id: int):
    return {"username": portfolio_id}