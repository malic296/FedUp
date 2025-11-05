import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv, find_dotenv
from pathlib import Path

this_dir = Path(__file__).resolve().parent 
env_path = this_dir.parent / "server.env" 

load_dotenv(dotenv_path=env_path, override=True)
load_dotenv(find_dotenv("server.env"))
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)