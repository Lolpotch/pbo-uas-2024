from sqlalchemy import Column, String
from database import Base, session

class Login(Base):
    __tablename__ = 'login'

    username = Column(String, primary_key=True)
    password = Column(String)

def login():
    print("--- Login ---")
    username = input("Username: ")
    password = input("Password: ")

    user = session.query(Login).filter_by(username=username, password=password).first()
    if user:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False