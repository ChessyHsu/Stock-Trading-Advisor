from typing import List
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.prices import Prices
from app.schemas.prices import Price, PriceIn


class CRUDItem(CRUDBase[Prices, Price, PriceIn]):
    def get_company_prices_by_date(
        self, db: Session, date, sortby, order) -> List[Prices]:
        cur = db.execute("SELECT * FROM price \
            WHERE timestamp = :timestamp\
            ORDER BY {} {}".format(sortby, order),\
             {'timestamp': date})
        return (
            cur.all()
        )

prices = CRUDItem(Prices)

