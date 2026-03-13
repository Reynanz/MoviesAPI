from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Data for accessing the database
DB_USER = "root"
DB_PASSWORD = ""
DB_HOST = "localhost"
DB_NAME = "moviesapi"

# MySQL connection URL via pymysql
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# Creating the engine
engine = create_engine(DATABASE_URL, echo=True, future=True)

# Creating the session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base for ORM models
Base = declarative_base()
