from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:Taranjeet303@localhost:5432/fastapi_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)