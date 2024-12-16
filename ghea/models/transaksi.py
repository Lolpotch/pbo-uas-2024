from data import Transaksi, Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc

class TransaksiOperations:
    def __init__(self):
        self.session = Session()

    # CREATE
    def tambah_data(self, idTransaksi, tanggal, pelanggan, jenisBarang, jumlah, status):
        try:
            jumlah = int(jumlah)
            if jumlah <= 0:
                raise ValueError("Jumlah harus lebih dari 0!")
            new_transaksi = Transaksi(
                idTransaksi=idTransaksi.strip().upper(),
                Tanggal=tanggal,
                NamaPelanggan=pelanggan.title(),
                JenisBarang=jenisBarang.title(),
                Jumlah=jumlah,
                StatusBayar=status.capitalize()
            )
            self.session.add(new_transaksi)
            self.session.commit()
            return "Data Transaksi berhasil ditambahkan!"
        except exc.IntegrityError:
            self.session.rollback()
            return "ID Transaksi sudah ada!"
        except ValueError as e:
            return f"Error: {e}"
        except Exception as e:
            self.session.rollback()
            return f"Database Error: {str(e)}"

    # READ
    def cari_data(self, idTransaksi):
        try:
            transaksi = self.session.query(Transaksi).filter(Transaksi.idTransaksi == idTransaksi).first()
            if transaksi:
                return transaksi
            else:
                return "Transaksi tidak ditemukan!"
        except Exception as e:
            return f"Error: {str(e)}"

    # UPDATE
    def ubah_data(self, idTransaksi, tanggal, pelanggan, jenisBarang, jumlah, status):
        try:
            transaksi = self.session.query(Transaksi).filter(Transaksi.idTransaksi == idTransaksi).first()
            if transaksi:
                transaksi.Tanggal = tanggal
                transaksi.NamaPelanggan = pelanggan.title()
                transaksi.JenisBarang = jenisBarang.title()
                transaksi.Jumlah = int(jumlah)
                transaksi.StatusBayar = status.capitalize()
                self.session.commit()
                return "Data Transaksi berhasil diperbarui!"
            else:
                return "Transaksi tidak ditemukan!"
        except Exception as e:
            self.session.rollback()
            return f"Error: {str(e)}"

    # DELETE
    def hapus_data(self, idTransaksi):
        try:
            transaksi = self.session.query(Transaksi).filter(Transaksi.idTransaksi == idTransaksi).first()
            if transaksi:
                self.session.delete(transaksi)
                self.session.commit()
                return "Data Transaksi berhasil dihapus!"
            else:
                return "Transaksi tidak ditemukan!"
        except Exception as e:
            self.session.rollback()
            return f"Error: {str(e)}"
