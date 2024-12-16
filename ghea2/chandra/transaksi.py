from sqlalchemy import Column, Integer, String, Date
from database import Base

class Transaksi(Base):
    __tablename__ = 'transaksi'

    id_transaksi = Column(Integer, primary_key=True)
    tanggal = Column(Date)
    nama_pelanggan = Column(String)
    jenis_barang = Column(String)
    jumlah = Column(Integer)
    stat_bayar = Column(String)