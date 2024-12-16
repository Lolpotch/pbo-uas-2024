from datetime import date
from modelss.data import Data

class Laporan(Data):
    def __init__(self, id_laporan: int, alamat_kirim: str, deskripsi: str, tanggal: date):
        self.id_laporan = id_laporan
        self.alamat_kirim = alamat_kirim
        self.deskripsi = deskripsi
        self.tanggal = tanggal

    def TambahData(self):
        print("Laporan ditambahkan")

    def EditData(self):
        print("Laporan diedit")

    def HapusData(self):
        print("Laporan dihapus")

    def CariData(self):
        print("Laporan dicari")