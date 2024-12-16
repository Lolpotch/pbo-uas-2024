from data import Barang, Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc

class BarangOperations:
    def __init__(self):
        self.session = Session()

    # CREATE
    def tambah_data(self, idBarang, jenisBarang, stok, masuk, keluar, tanggal):
        try:
            stok = int(stok)
            masuk = int(masuk)
            keluar = int(keluar)
            if stok < 0 or masuk < 0 or keluar < 0:
                raise ValueError("Nilai tidak boleh negatif!")
            new_barang = Barang(
                idBarang=idBarang.strip().upper(),
                JenisBarang=jenisBarang.title(),
                StokGudang=stok,
                BarangMasuk=masuk,
                BarangKeluar=keluar,
                Tanggal=tanggal
            )
            self.session.add(new_barang)
            self.session.commit()
            return "Data Barang berhasil ditambahkan!"
        except exc.IntegrityError:
            self.session.rollback()
            return "ID Barang sudah ada!"
        except ValueError as e:
            return f"Error: {e}"
        except Exception as e:
            self.session.rollback()
            return f"Database Error: {str(e)}"

    # READ
    def cari_data(self, idBarang):
        try:
            barang = self.session.query(Barang).filter(Barang.idBarang == idBarang).first()
            if barang:
                return barang
            else:
                return "Barang tidak ditemukan!"
        except Exception as e:
            return f"Error: {str(e)}"

    # UPDATE
    def ubah_data(self, idBarang, jenisBarang, stok, masuk, keluar, tanggal):
        try:
            barang = self.session.query(Barang).filter(Barang.idBarang == idBarang).first()
            if barang:
                barang.JenisBarang = jenisBarang.title()
                barang.StokGudang = int(stok)
                barang.BarangMasuk = int(masuk)
                barang.BarangKeluar = int(keluar)
                barang.Tanggal = tanggal
                self.session.commit()
                return "Data Barang berhasil diperbarui!"
            else:
                return "Barang tidak ditemukan!"
        except Exception as e:
            self.session.rollback()
            return f"Error: {str(e)}"

    # DELETE
    def hapus_data(self, idBarang):
        try:
            barang = self.session.query(Barang).filter(Barang.idBarang == idBarang).first()
            if barang:
                self.session.delete(barang)
                self.session.commit()
                return "Data Barang berhasil dihapus!"
            else:
                return "Barang tidak ditemukan!"
        except Exception as e:
            self.session.rollback()
            return f"Error: {str(e)}"
