# from modelss.dashboard import Dashboard

# if __name__ == "__main__":
#     Dashboard.login()
#     Dashboard.show_menu()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelss.transaksi import Base  # Assuming Transaksi and other models are in transaksi.py

# Step 1: Define the database file
DATABASE_URL = "sqlite:///pbo-uas-24.db"  # This creates an SQLite file named 'my_database.db'

# Step 2: Create the engine
engine = create_engine(DATABASE_URL, echo=True)  # echo=True enables logging of SQL queries

# Step 3: Create all tables in the database
Base.metadata.create_all(engine)

# Step 4: Set up a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()