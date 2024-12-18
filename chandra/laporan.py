from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.types import Integer, Date
from datetime import datetime
from database import Base

class Laporan(Base):
    __tablename__ = 'laporan'

    id_laporan = Column(Integer, primary_key=True)
    alamat_kirim = Column(String)
    deskripsi = Column(String)
    tanggal = Column(Date)

    def add_data(self):
        print(f"--- Add Data to {Laporan.__tablename__.capitalize()} ---")
        data = {}
        for column in Laporan.__table__.columns:
            if column.name != Laporan.__table__.primary_key.columns.keys()[0]:
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

        self.session.add(Laporan(**data))
        self.session.commit()
        print("Data added successfully.")
        
    def edit_data(self):
        print(f"--- Edit Data in {Laporan.__tablename__.capitalize()} ---")
        id_value = input(f"Enter the ID of the record to edit ({Laporan.__table__.primary_key.columns.keys()[0]}): ")
        record = self.session.query(Laporan).get(id_value)
        if not record:
            print("Record not found.")
            return

        for column in Laporan.__table__.columns:
            if column.name != Laporan.__table__.primary_key.columns.keys()[0]:
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
        print(f"--- Delete Data from {Laporan.__tablename__.capitalize()} ---")
        try:
            id_value = input(f"Enter the ID of the record to edit ({Laporan.__table__.primary_key.columns.keys()[0]}): ")
            record = self.session.query(Laporan).get(id_value)
            #self.session.query untuk mencari data dlm bentuk id_value dlm model/tabel
            if not record:
                raise ValueError("Record not found.")

            self.session.delete(record)
            self.session.commit()
            print("Data deleted successfully.")
        except ValueError as ve:
            print(ve)

    def search_data(self):
        print(f"--- Search Data in {Laporan.__tablename__.capitalize()} ---")
        search_value = input("Enter the date to search (YYYY-MM-DD): ")
        try:
            search_date = datetime.strptime(search_value, "%Y-%m-%d").date()
            results = self.session.query(Laporan).filter(Laporan.tanggal == search_date).all()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return

        if not results:
            print("No matching records found.")
            return

        for row in results:
            print(" | ".join(f"{key}: {value}" for key, value in row.__dict__.items() if key != '_sa_instance_state'))
