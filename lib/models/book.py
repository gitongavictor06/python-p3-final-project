from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer)
    rating = Column(Integer)
    review = Column(String)

    genre_id = Column(Integer, ForeignKey('genres.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    genre = relationship("Genre")
    user = relationship("User")

    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', author='{self.author}', rating={self.rating})>"
