from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base for SQLAlchemy models
Base = declarative_base()

# Database setup
db_url = 'sqlite:///inventory.db'
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()