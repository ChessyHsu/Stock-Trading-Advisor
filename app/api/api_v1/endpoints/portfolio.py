from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_portfolios():
    return {"username": "fakecurrentuser"}


@router.get("/{portfolio_id}")
async def get_portfolio(portfolio_id: int):
    return {"username": portfolio_id}