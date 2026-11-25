from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from os import environ

# Database URL for SQLite
# engine = create_engine(
#    "sqlite:///./test.db", connect_args={"check_same_thread": False})

# Database URL for Postgres
engine = create_engine(environ.get("DATABASE_URL", "sqlite:///./test.db"))

# Create a SessionLocal class for database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class for our models
Base = declarative_base()
