from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import BaseConfig

engine = create_engine('postgresql://postgres:toor@localhost:5432/lidiski')
Session = sessionmaker(bind=engine)
session = Session()