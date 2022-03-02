from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Notes(Base):
    id = Column("id", Integer, primary_key=True)
    text = Column(String)
    completed = Column(Boolean)