from sqlalchemy import Column, Integer, String, Date
from database import Base

class Barang(Base):
    __tablename__ = 'barang'

    id_barang = Column(Integer, primary_key=True)
    jenis_barang = Column(String)
    stok_gudang = Column(Integer)
    barang_masuk = Column(Integer)
    barang_keluar = Column(Integer)
    tanggal = Column(Date)