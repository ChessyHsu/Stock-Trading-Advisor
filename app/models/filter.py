from sqlalchemy import Column, String

from app.db.base_class import Base


class Filter(Base):
    filter_name = Column(String, primary_key=True)
    type = Column(String)
    table_name = Column(String)
