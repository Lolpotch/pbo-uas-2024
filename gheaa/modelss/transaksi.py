from datetime import date
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Transaksi(Base):
    __tablename__ = 'transaksi'

    id_transaksi = Column(Integer, primary_key=True, autoincrement=True)
    tanggal = Column(Date, default=date.today)
    nama_pelanggan = Column(String(255), nullable=False)
    jenis_barang = Column(String(255), nullable=False)
    jumlah = Column(Integer, nullable=False)
    stat_bayar = Column(String(50), nullable=False)

    def __init__(self, tanggal: date, nama_pelanggan: str, jenis_barang: str, jumlah: int, stat_bayar: str):
        self.tanggal = tanggal
        self.nama_pelanggan = nama_pelanggan
        self.jenis_barang = jenis_barang
        self.jumlah = jumlah
        self.stat_bayar = stat_bayar

    def TambahData(self, session):
        session.add(self)
        session.commit()
        print("Transaksi ditambahkan")

    def EditData(self, session, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        session.commit()
        print("Transaksi diedit")

    def HapusData(self, session):
        session.delete(self)
        session.commit()
        print("Transaksi dihapus")

    @staticmethod
    def CariData(session, id_transaksi):
        transaksi = session.query(Transaksi).filter_by(id_transaksi=id_transaksi).first()
        if transaksi:
            print(f"Transaksi ditemukan: {transaksi}")
        else:
            print("Transaksi tidak ditemukan")
        return transaksi