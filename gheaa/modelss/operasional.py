from datetime import date
from sqlalchemy import Column, Integer, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Operasional(Base):
    __tablename__ = 'operasional'

    id_transaksi = Column(Integer, primary_key=True, autoincrement=True)
    tanggal = Column(Date, default=date.today)
    biaya_mobil = Column(Integer, nullable=False)
    biaya_supir = Column(Integer, nullable=False)
    total_biaya = Column(Integer, nullable=False)

    def __init__(self, tanggal: date, biaya_mobil: int, biaya_supir: int, total_biaya: int):
        self.tanggal = tanggal
        self.biaya_mobil = biaya_mobil
        self.biaya_supir = biaya_supir
        self.total_biaya = total_biaya

    def TambahData(self, session):
        session.add(self)
        session.commit()
        print("Data operasional ditambahkan")

    def EditData(self, session, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        session.commit()
        print("Data operasional diedit")

    def HapusData(self, session):
        session.delete(self)
        session.commit()
        print("Data operasional dihapus")

    @staticmethod
    def CariData(session, id_transaksi):
        operasional = session.query(Operasional).filter_by(id_transaksi=id_transaksi).first()
        if operasional:
            print(f"Data operasional ditemukan: {operasional}")
        else:
            print("Data operasional tidak ditemukan")
        return operasional
