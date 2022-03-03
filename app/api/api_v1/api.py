from fastapi import APIRouter
from app.api.api_v1.endpoints import portfolio, notes, screeners

api_router = APIRouter()
api_router.include_router(portfolio.router, prefix="/portfolio", tags=["portfolio"])
api_router.include_router(screeners.router, prefix="/screeners", tags=["screeners"])
api_router.include_router(notes.router, prefix="/notes", tags=["test"])