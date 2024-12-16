from abc import ABC
from datetime import date
from data import Data

class Laporan(Data):
    def __init__(self, idLaporan: int, alamatKirim: str, deskripsi: str, tanggal: date):
        self.idLaporan = idLaporan
        self.alamatKirim = alamatKirim
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