from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.types import Integer, Date
from datetime import datetime
from database import Base

class Barang(Base):
    __tablename__ = 'barang'

    id_barang = Column(Integer, primary_key=True)
    jenis_barang = Column(String)
    stok_gudang = Column(Integer)
    barang_masuk = Column(Integer)
    barang_keluar = Column(Integer)
    tanggal = Column(Date)

    def add_data(self):
        print(f"--- Add Data to {Barang.__tablename__.capitalize()} ---")
        data = {}
        for column in Barang.__table__.columns:
            if column.name != Barang.__table__.primary_key.columns.keys()[0]:
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

        self.session.add(Barang(**data))
        self.session.commit()
        print("Data added successfully.")
    
    def edit_data(self):
        print(f"--- Edit Data in {Barang.__tablename__.capitalize()} ---")
        id_value = input(f"Enter the ID of the record to edit ({Barang.__table__.primary_key.columns.keys()[0]}): ")
        record = self.session.query(Barang).get(id_value)
        if not record:
            print("Record not found.")
            return

        for column in Barang.__table__.columns:
            if column.name != Barang.__table__.primary_key.columns.keys()[0]:
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
        print(f"--- Delete Data from {Barang.__tablename__.capitalize()} ---")
        try:
            id_value = input(f"Enter the ID of the record to delete ({Barang.__table__.primary_key.columns.keys()[0]}): ")
            record = self.session.query(Barang).get(id_value)
            #self.session.query untuk mencari data dlm bentuk id_value dlm model/tabel
            if not record:
                raise ValueError("Record not found.")

            self.session.delete(record)
            self.session.commit()
            print("Data deleted successfully.")
        except ValueError as ve:
            print(ve)

    def search_data(self):
        print(f"--- Search Data in {Barang.__tablename__.capitalize()} ---")
        try:
            search_value = input("Enter the name of the item to search (jenis_barang): ")
            results = self.session.query(Barang).filter(Barang.jenis_barang.like(f"%{search_value}%")).all()
        except ValueError:
            print("Invalid item name.")
            return

        if not results:
            print("No matching records found.")
            return
        
        for row in results:
            print(" | ".join(f"{key}: {value}" for key, value in row.__dict__.items() if key != '_sa_instance_state'))
