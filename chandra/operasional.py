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