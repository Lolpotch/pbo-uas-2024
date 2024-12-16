from sqlalchemy import Column, Integer, String, Date
from database import Base

class Laporan(Base):
    __tablename__ = 'laporan'

    id_laporan = Column(Integer, primary_key=True)
    alamat_kirim = Column(String)
    deskripsi = Column(String)
    tanggal = Column(Date)