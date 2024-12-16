from datetime import date
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Barang(Base):
    __tablename__ = 'barang'

    id_barang = Column(Integer, primary_key=True, autoincrement=True)
    jenis_barang = Column(String(100), nullable=False)
    stok_gudang = Column(Integer, nullable=False)
    barang_masuk = Column(Integer, nullable=False)
    barang_keluar = Column(Integer, nullable=False)
    tanggal = Column(Date, default=date.today)

    def __init__(self, jenis_barang: str, stok_gudang: int, barang_masuk: int, barang_keluar: int, tanggal: date = date.today()):
        self.jenis_barang = jenis_barang
        self.stok_gudang = stok_gudang
        self.barang_masuk = barang_masuk
        self.barang_keluar = barang_keluar
        self.tanggal = tanggal

    def TambahData(self, session):
        session.add(self)
        session.commit()
        print("Barang ditambahkan")

    def EditData(self, session, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        session.commit()
        print("Barang diedit")

    def HapusData(self, session):
        session.delete(self)
        session.commit()
        print("Barang dihapus")

    @staticmethod
    def CariData(session, id_barang):
        barang = session.query(Barang).filter_by(id_barang=id_barang).first()
        if barang:
            print(f"Barang ditemukan: {barang}")
        else:
            print("Barang tidak ditemukan")
        return barang