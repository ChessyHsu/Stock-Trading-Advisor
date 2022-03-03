# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base
from app.models.notes import Notes 
from app.models.account import Account
from app.models.portfolio import Portfolio, PortfolioStock