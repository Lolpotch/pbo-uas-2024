from datetime import date
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Laporan(Base):
    __tablename__ = 'laporan'

    id_laporan = Column(Integer, primary_key=True, autoincrement=True)
    alamat_kirim = Column(String(255), nullable=False)
    deskripsi = Column(String(500), nullable=False)
    tanggal = Column(Date, default=date.today)

    def __init__(self, alamat_kirim: str, deskripsi: str, tanggal: date = date.today()):
        self.alamat_kirim = alamat_kirim
        self.deskripsi = deskripsi
        self.tanggal = tanggal

    def TambahData(self, session):
        session.add(self)
        session.commit()
        print("Laporan ditambahkan")

    def EditData(self, session, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        session.commit()
        print("Laporan diedit")

    def HapusData(self, session):
        session.delete(self)
        session.commit()
        print("Laporan dihapus")

    @staticmethod
    def CariData(session, id_laporan):
        laporan = session.query(Laporan).filter_by(id_laporan=id_laporan).first()
        if laporan:
            print(f"Laporan ditemukan: {laporan}")
        else:
            print("Laporan tidak ditemukan")
        return laporan
