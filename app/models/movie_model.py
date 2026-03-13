from sqlalchemy import Column, Integer, String
from app.database.connection import Base


# Film model
class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(50))
    year = Column(Integer)
    genre = Column(String(20))
