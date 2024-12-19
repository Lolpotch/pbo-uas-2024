from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.types import Integer, Date
from datetime import datetime
from database import Base

class Transaksi(Base):
    __tablename__ = 'transaksi'

    id_transaksi = Column(Integer, primary_key=True)
    tanggal = Column(Date)
    nama_pelanggan = Column(String)
    jenis_barang = Column(String)
    jumlah = Column(Integer)
    stat_bayar = Column(String)

    def add_data(self):
        print(f"--- Add Data to {Transaksi.__tablename__.capitalize()} ---")
        data = {}
        for column in Transaksi.__table__.columns:
            if column.name != Transaksi.__table__.primary_key.columns.keys()[0]:
                while True:
                    value = input(f"Enter {column.name}: ")
                    if isinstance(column.type, Date):
                        try:
                            value = datetime.strptime(value, "%Y-%m-%d").date()
                        except ValueError:
                            print("Invalid date format. Please use YYYY-MM-DD.")
                            continue
                    elif isinstance(column.type, Integer):
                        try:
                            value = int(value)
                        except ValueError:
                            print("Invalid integer. Please enter a valid integer value.")
                            continue
                    # If the input is valid, break out of the loop
                    break
                data[column.name] = value

        self.session.add(Transaksi(**data))
        self.session.commit()
        print("Data added successfully.")
    
    def edit_data(self):
        print(f"--- Edit Data in {Transaksi.__tablename__.capitalize()} ---")
        id_value = input(f"Enter the ID of the record to edit ({Transaksi.__table__.primary_key.columns.keys()[0]}): ")
        record = self.session.query(Transaksi).get(id_value)
        if not record:
            print("Record not found.")
            return

        for column in Transaksi.__table__.columns:
            if column.name != Transaksi.__table__.primary_key.columns.keys()[0]:
                value = input(f"Enter new {column.name} (leave blank to keep current): ")
                if value:
                    if isinstance(column.type, Date):
                        try:
                            value = datetime.strptime(value, "%Y-%m-%d").date()
                        except ValueError:
                            print("Invalid date format. Please use YYYY-MM-DD.")
                            return
                    setattr(record, column.name, value)
        self.session.commit()
        print("Data updated successfully.")
    
    def delete_data(self):
        print(f"--- Delete Data from {Transaksi.__tablename__.capitalize()} ---")
        try:
            id_value = input(f"Enter the ID of the record to delete ({Transaksi.__table__.primary_key.columns.keys()[0]}): ")
            record = self.session.query(Transaksi).get(id_value)
            #self.session.query untuk mencari data dlm bentuk id_value dlm model/tabel
            if not record:
                raise ValueError("Record not found.")

            self.session.delete(record)
            self.session.commit()
            print("Data deleted successfully.")
        except ValueError as ve:
            print(ve)

    def search_data(self):
        print(f"--- Search Data in {Transaksi.__tablename__.capitalize()} ---")
        try:
            search_value = input("Enter the name of the customer to search (nama_pelanggan): ")
            results = self.session.query(Transaksi).filter(Transaksi.nama_pelanggan.like(f"%{search_value}%")).all()     
        except ValueError:
            print("Invalid name of customer.")
            return

        if not results:
            print("No matching records found.")
            return
        
        for row in results:
            print(" | ".join(f"{key}: {value}" for key, value in row.__dict__.items() if key != '_sa_instance_state'))
