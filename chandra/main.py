from sqlalchemy import Column, Integer, String, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime


# Base for SQLAlchemy models
Base = declarative_base()

# Database models
class Barang(Base):
    __tablename__ = 'barang'

    id_barang = Column(Integer, primary_key=True)
    jenis_barang = Column(String)
    stok_gudang = Column(Integer)
    barang_masuk = Column(Integer)
    barang_keluar = Column(Integer)
    tanggal = Column(Date)

class Transaksi(Base):
    __tablename__ = 'transaksi'

    id_transaksi = Column(Integer, primary_key=True)
    tanggal = Column(Date)
    nama_pelanggan = Column(String)
    jenis_barang = Column(String)
    jumlah = Column(Integer)
    stat_bayar = Column(String)

class Operasional(Base):
    __tablename__ = 'operasional'

    id_transaksi = Column(Integer, primary_key=True)
    tanggal = Column(Date)
    biaya_mobil = Column(Integer)
    biaya_supir = Column(Integer)
    total_biaya = Column(Integer)

class Laporan(Base):
    __tablename__ = 'laporan'

    id_laporan = Column(Integer, primary_key=True)
    alamat_kirim = Column(String)
    deskripsi = Column(String)
    tanggal = Column(Date)

class Login(Base):
    __tablename__ = 'login'

    username = Column(String, primary_key=True)
    password = Column(String)

# Database setup
db_url = 'sqlite:///inventory.db'
engine = create_engine(db_url)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# session.add(Login(username='admin', password='password123'))
# session.commit()

# Dashboard class for operations
class Dashboard:
    def __init__(self):
        self.session = session

    def show_data(self, model):
        print(f"--- Data {model.__tablename__.capitalize()} ---")
        data = self.session.query(model).all()
        if not data:
            print("No data available.")
            return

        for row in data:
            print(" | ".join(f"{key}: {value}" for key, value in row.__dict__.items() if key != '_sa_instance_state'))


    def add_data(self, model):
        print(f"--- Add Data to {model.__tablename__.capitalize()} ---")
        data = {}
        for column in model.__table__.columns:
            if column.name != model.__table__.primary_key.columns.keys()[0]:
                value = input(f"Enter {column.name}: ")
                # Convert to date if the column is a Date type
                if isinstance(column.type, Date):
                    try:
                        value = datetime.strptime(value, "%Y-%m-%d").date()
                    except ValueError:
                        print("Invalid date format. Please use YYYY-MM-DD.")
                        return
                data[column.name] = value
        self.session.add(model(**data))
        self.session.commit()
        print("Data added successfully.")


    def edit_data(self, model):
        print(f"--- Edit Data in {model.__tablename__.capitalize()} ---")
        id_value = input(f"Enter the ID of the record to edit ({model.__table__.primary_key.columns.keys()[0]}): ")
        record = self.session.query(model).get(id_value)
        if not record:
            print("Record not found.")
            return

        for column in model.__table__.columns:
            if column.name != model.__table__.primary_key.columns.keys()[0]:
                value = input(f"Enter new {column.name} (leave blank to keep current): ")
                if value:
                    # Convert to date if the column is a Date type
                    if isinstance(column.type, Date):
                        try:
                            value = datetime.strptime(value, "%Y-%m-%d").date()
                        except ValueError:
                            print("Invalid date format. Please use YYYY-MM-DD.")
                            return
                    setattr(record, column.name, value)
        self.session.commit()
        print("Data updated successfully.")


    def delete_data(self, model):
        print(f"--- Delete Data from {model.__tablename__.capitalize()} ---")
        id_value = input(f"Enter the ID of the record to delete ({model.__table__.primary_key.columns.keys()[0]}): ")
        record = self.session.query(model).get(id_value)
        if not record:
            print("Record not found.")
            return

        self.session.delete(record)
        self.session.commit()
        print("Data deleted successfully.")

    def search_data(self, model):
        print(f"--- Search Data in {model.__tablename__.capitalize()} ---")
        search_field = input("Enter the field to search: ")
        search_value = input("Enter the value to search for: ")
        results = self.session.query(model).filter(getattr(model, search_field).like(f"%{search_value}%")).all()
        if not results:
            print("No matching records found.")
            return

        for row in results:
            print(" | ".join(f"{key}: {value}" for key, value in row.__dict__.items() if key != '_sa_instance_state'))

    def manage_data(self, model):
        while True:
            print(f"\nManage {model.__tablename__.capitalize()}:")
            print("1. Add Data")
            print("2. Edit Data")
            print("3. Delete Data")
            print("4. Search Data")
            print("5. Back to Dashboard")
            choice = input("Choose an option: ")

            if choice == "1":
                self.add_data(model)

            elif choice == "2":
                self.edit_data(model)

            elif choice == "3":
                self.delete_data(model)

            elif choice == "4":
                self.search_data(model)

            elif choice == "5":
                break

            else:
                print("Invalid choice, please try again.")

    def main_menu(self):
        while True:
            print("\n--- Dashboard ---")
            print("1. Show Data Barang")
            print("2. Show Data Transaksi")
            print("3. Show Data Operasional")
            print("4. Show Data Laporan")
            print("5. Manage Barang")
            print("6. Manage Transaksi")
            print("7. Manage Operasional")
            print("8. Manage Laporan")
            print("9. Logout")
            choice = input("Choose an option: ")

            if choice == "1":
                self.show_data(Barang)
            elif choice == "2":
                self.show_data(Transaksi)
            elif choice == "3":
                self.show_data(Operasional)
            elif choice == "4":
                self.show_data(Laporan)
            elif choice == "5":
                self.manage_data(Barang)
            elif choice == "6":
                self.manage_data(Transaksi)
            elif choice == "7":
                self.manage_data(Operasional)
            elif choice == "8":
                self.manage_data(Laporan)
            elif choice == "9":
                print("Logging out...")
                break
            else:
                print("Invalid choice, please try again.")

# Login system
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

# Main program
def main():
    while not login():
        pass

    dashboard = Dashboard()
    dashboard.main_menu()

if __name__ == "__main__":
    main()