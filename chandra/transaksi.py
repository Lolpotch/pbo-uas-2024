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