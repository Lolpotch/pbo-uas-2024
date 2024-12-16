from data import Operasional, Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc

class OperasionalOperations:
    def __init__(self):
        self.session = Session()

    # CREATE
    def tambah_data(self, idTransaksi, tanggal, biaya_mobil, biaya_supir):
        try:
            biaya_mobil = float(biaya_mobil)
            biaya_supir = float(biaya_supir)
            total = biaya_mobil + biaya_supir
            new_operasional = Operasional(
                idTransaksi=idTransaksi.strip().upper(),
                Tanggal=tanggal,
                BiayaMobil=biaya_mobil,
                BiayaSupir=biaya_supir,
                TotalBiaya=total
            )
            self.session.add(new_operasional)
            self.session.commit()
            return f"Data Operasional berhasil ditambahkan! Total Biaya: {total}"
        except exc.IntegrityError:
            self.session.rollback()
            return "ID Transaksi sudah ada!"
        except ValueError:
            return "Error: Biaya harus berupa angka!"
        except Exception as e:
            self.session.rollback()
            return f"Database Error: {str(e)}"

    # READ
    def cari_data(self, idTransaksi):
        try:
            operasional = self.session.query(Operasional).filter(Operasional.idTransaksi == idTransaksi).first()
            if operasional:
                return operasional
            else:
                return "Data Operasional tidak ditemukan!"
        except Exception as e:
            return f"Error: {str(e)}"

    # UPDATE
    def ubah_data(self, idTransaksi, biaya_mobil, biaya_supir):
        try:
            operasional = self.session.query(Operasional).filter(Operasional.idTransaksi == idTransaksi).first()
            if operasional:
                operasional.BiayaMobil = float(biaya_mobil)
                operasional.BiayaSupir = float(biaya_supir)
                operasional.TotalBiaya = operasional.BiayaMobil + operasional.BiayaSupir
                self.session.commit()
                return "Data Operasional berhasil diperbarui!"
            else:
                return "Data Operasional tidak ditemukan!"
        except Exception as e:
            self.session.rollback()
            return f"Error: {str(e)}"

    # DELETE
    def hapus_data(self, idTransaksi):
        try:
            operasional = self.session.query(Operasional).filter(Operasional.idTransaksi == idTransaksi).first()
            if operasional:
                self.session.delete(operasional)
                self.session.commit()
                return "Data Operasional berhasil dihapus!"
            else:
                return "Data Operasional tidak ditemukan!"
        except Exception as e:
            self.session.rollback()
            return f"Error: {str(e)}"
