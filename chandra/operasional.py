from sqlalchemy import Column, Integer, Date
from database import Base

class Operasional(Base):
    __tablename__ = 'operasional'

    id_transaksi = Column(Integer, primary_key=True)
    tanggal = Column(Date)
    biaya_mobil = Column(Integer)
    biaya_supir = Column(Integer)
    total_biaya = Column(Integer)