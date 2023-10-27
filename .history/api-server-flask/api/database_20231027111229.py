from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://postgres:root@localhost:5432/lidiski')
Session = sessionmaker(bind=engine)
session = Session()