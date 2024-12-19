from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.types import Integer, Date
from datetime import datetime
from database import Base

class Operasional(Base):
    __tablename__ = 'operasional'

    id_transaksi = Column(Integer, primary_key=True)
    tanggal = Column(Date)
    biaya_mobil = Column(Integer)
    biaya_supir = Column(Integer)
    total_biaya = Column(Integer)

    def add_data(self):
        print(f"--- Add Data to {Operasional.__tablename__.capitalize()} ---")
        data = {}
        for column in Operasional.__table__.columns:
            if column.name != Operasional.__table__.primary_key.columns.keys()[0]:
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

        self.session.add(Operasional(**data))
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

    def search_data(self):
        print(f"--- Search Data in {Operasional.__tablename__.capitalize()} ---")
        search_value = input("Enter the date to search (YYYY-MM-DD): ")
        try:
            search_date = datetime.strptime(search_value, "%Y-%m-%d").date()
            results = self.session.query(Operasional).filter(Operasional.tanggal == search_date).all()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return
        
        if not results:
            print("No matching records found.")
            return

        for row in results:
            print(" | ".join(f"{key}: {value}" for key, value in row.__dict__.items() if key != '_sa_instance_state'))
