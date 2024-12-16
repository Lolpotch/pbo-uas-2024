from abc import ABC, abstractmethod
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Abstract Class & Interface
class Data(ABC):
    @abstractmethod
    def tambah_data(self, *args, **kwargs):
        pass

    def edit_data(self):
        pass

    def hapus_data(self):
        pass

    def cari_data(self):
        pass

# Setup Database Connection
DATABASE_URL = "sqlite:///inventory_system.db"  # SQLite database file

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# Define Tables for SQLAlchemy

class Barang(Base):
    __tablename__ = 'barang'

    idBarang = Column(String, primary_key=True)
    JenisBarang = Column(String)
    StokGudang = Column(Integer)
    BarangMasuk = Column(Integer)
    BarangKeluar = Column(Integer)
    Tanggal = Column(Date)

    def __repr__(self):
        return f"<Barang(idBarang={self.idBarang}, JenisBarang={self.JenisBarang})>"

class Transaksi(Base):
    __tablename__ = 'transaksi'

    idTransaksi = Column(String, primary_key=True)
    Tanggal = Column(Date)
    NamaPelanggan = Column(String)
    JenisBarang = Column(String)
    Jumlah = Column(Integer)
    StatusBayar = Column(String)

    def __repr__(self):
        return f"<Transaksi(idTransaksi={self.idTransaksi}, NamaPelanggan={self.NamaPelanggan})>"

class Operasional(Base):
    __tablename__ = 'operasional'

    idTransaksi = Column(String, primary_key=True)
    Tanggal = Column(Date)
    BiayaMobil = Column(Float)
    BiayaSupir = Column(Float)
    TotalBiaya = Column(Float)

    def __repr__(self):
        return f"<Operasional(idTransaksi={self.idTransaksi}, TotalBiaya={self.TotalBiaya})>"

class Laporan(Base):
    __tablename__ = 'laporan'

    idLaporan = Column(String, primary_key=True)
    AlamatKirim = Column(String)
    Deskripsi = Column(String)
    Tanggal = Column(Date)

    def __repr__(self):
        return f"<Laporan(idLaporan={self.idLaporan}, AlamatKirim={self.AlamatKirim})>"

# Create the database tables
Base.metadata.create_all(engine)
