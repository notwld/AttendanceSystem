import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = os.getenv("DB_CONN")

engine = create_engine("postgresql://postgres:cqUAtB6zuPQM3HrtM0Vu@containers-us-west-53.railway.app:6135/railway")
SessionLocal = sessionmaker(autocommit=True, autoflush=False, bind=engine)

Base = declarative_base()