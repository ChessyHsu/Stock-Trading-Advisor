from sqlalchemy import Column, Integer, String

from app.db.base_class import Base

class Account(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)