from sqlalchemy import Column, Integer, String
from . import Base

class Genre(Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f"<Genre(id={self.id}, name='{self.name}')>"
