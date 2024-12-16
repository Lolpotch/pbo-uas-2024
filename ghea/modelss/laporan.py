from data import Laporan, Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc

class LaporanOperations:
    def __init__(self):
        self.session = Session()

    # CREATE
    def tambah_data(self, idLaporan, alamat, deskripsi, tanggal):
        new_laporan = Laporan(
            idLaporan=idLaporan.strip().upper(),
            AlamatKirim=alamat.title(),
            Deskripsi=deskripsi.capitalize(),
            Tanggal=tanggal
        )
        try:
            self.session.add(new_laporan)
            self.session.commit()
            return "Data Laporan berhasil ditambahkan!"
        except exc.IntegrityError:
            self.session.rollback()
            return "ID Laporan sudah ada!"
        except Exception as e:
            self.session.rollback()
            return f"Database Error: {str(e)}"

    # READ
    def cari_data(self, idLaporan):
        try:
            laporan = self.session.query(Laporan).filter(Laporan.idLaporan == idLaporan).first()
            if laporan:
                return laporan
            else:
                return "Data Laporan tidak ditemukan!"
        except Exception as e:
            return f"Error: {str(e)}"

    # UPDATE
    def ubah_data(self, idLaporan, alamat, deskripsi, tanggal):
        try:
            laporan = self.session.query(Laporan).filter(Laporan.idLaporan == idLaporan).first()
            if laporan:
                laporan.AlamatKirim = alamat.title()
                laporan.Deskripsi = deskripsi.capitalize()
                laporan.Tanggal = tanggal
                self.session.commit()
                return "Data Laporan berhasil diperbarui!"
            else:
                return "Data Laporan tidak ditemukan!"
        except Exception as e:
            self.session.rollback()
            return f"Error: {str(e)}"

    # DELETE
    def hapus_data(self, idLaporan):
        try:
            laporan = self.session.query(Laporan).filter(Laporan.idLaporan == idLaporan).first()
            if laporan:
                self.session.delete(laporan)
                self.session.commit()
                return "Data Laporan berhasil dihapus!"
            else:
                return "Data Laporan tidak ditemukan!"
        except Exception as e:
            self.session.rollback()
            return f"Error: {str(e)}"

