from database import Database
from sqlalchemy import crate_engin , MetaData # type: ignore
from dotenv import load_dotenv  # type: ignore
import os 

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Async Database instance
database = Database(DATABASE_URL)
metadata = MetaData()