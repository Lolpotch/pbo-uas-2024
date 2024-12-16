from models.data import User, Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc
from werkzeug.security import generate_password_hash, check_password_hash

class UserOperations:
    def __init__(self):
        self.session = Session()

    # CREATE (Register User)
    def register_user(self, username, password, email):
        try:
            hashed_password = generate_password_hash(password, method='sha256')
            new_user = User(
                username=username.strip(),
                password=hashed_password,
                email=email.strip().lower()
            )
            self.session.add(new_user)
            self.session.commit()
            return "User berhasil terdaftar!"
        except exc.IntegrityError:
            self.session.rollback()
            return "Username atau email sudah terdaftar!"
        except Exception as e:
            self.session.rollback()
            return f"Database Error: {str(e)}"

    # READ (Login User)
    def login_user(self, username, password):
        try:
            user = self.session.query(User).filter(User.username == username).first()
            if user and check_password_hash(user.password, password):
                return "Login berhasil!"
            elif user:
                return "Password salah!"
            else:
                return "Username tidak ditemukan!"
        except Exception as e:
            return f"Error: {str(e)}"

    # READ (Cek Data Pengguna)
    def get_user_data(self, username):
        try:
            user = self.session.query(User).filter(User.username == username).first()
            if user:
                return {
                    "Username": user.username,
                    "Email": user.email
                }
            else:
                return "User tidak ditemukan!"
        except Exception as e:
            return f"Error: {str(e)}"

    # UPDATE (Mengubah Password Pengguna)
    def update_password(self, username, old_password, new_password):
        try:
            user = self.session.query(User).filter(User.username == username).first()
            if user and check_password_hash(user.password, old_password):
                user.password = generate_password_hash(new_password, method='sha256')
                self.session.commit()
                return "Password berhasil diperbarui!"
            elif user:
                return "Password lama salah!"
            else:
                return "Username tidak ditemukan!"
        except Exception as e:
            self.session.rollback()
            return f"Error: {str(e)}"

    # DELETE (Menghapus User)
    def delete_user(self, username, password):
        try:
            user = self.session.query(User).filter(User.username == username).first()
            if user and check_password_hash(user.password, password):
                self.session.delete(user)
                self.session.commit()
                return "User berhasil dihapus!"
            elif user:
                return "Password salah!"
            else:
                return "Username tidak ditemukan!"
        except Exception as e:
            self.session.rollback()
            return f"Error: {str(e)}"
