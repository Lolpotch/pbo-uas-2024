from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Base and engine setup
Base = declarative_base()
engine = create_engine('sqlite:///example.db')  # Database file
Session = sessionmaker(bind=engine)
session = Session()

# Login model
class Login(Base):
    __tablename__ = 'login'
    username = Column(String, primary_key=True)
    password = Column(String)

# Create table
Base.metadata.create_all(engine)

def add_user(username, password):
    # Buat objek Login baru
    new_user = Login(username=username, password=password)

    # Tambahkan user ke session
    session.add(new_user)

    # Simpan perubahan ke database
    session.commit()
    print(f"User '{username}' berhasil ditambahkan!")

# Tambahkan user baru
add_user("user123", "password123")
add_user("admin", "admin123")

# Ambil semua user dari tabel login
users = session.query(Login).all()
for user in users:
    print(f"Username: {user.username}, Password: {user.password}")

# Login function
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
