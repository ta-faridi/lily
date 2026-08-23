from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = f"postgresql://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}:5432/{os.getenv("DB_NAME")}"
# educational comment: 
# why 5432?
# this format: 

engine = create_engine(DATABASE_URL)

session_local = sessionmaker(bind=engine)

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()