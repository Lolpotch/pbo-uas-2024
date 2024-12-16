from abc import ABC
from datetime import date
from data import Data

class Operasional(Data):
    def __init__(self, idTransaksi: int, tanggal: date, biayaMobil: int, biayaSupir: int, totalBiaya: int):
        self.idTransaksi = idTransaksi
        self.tanggal = tanggal
        self.biayaMobil = biayaMobil
        self.biayaSupir = biayaSupir
        self.totalBiaya = totalBiaya

    def TambahData(self):
        print("Data operasional ditambahkan")

    def EditData(self):
        print("Data operasional diedit")

    def HapusData(self):
        print("Data operasional dihapus")

    def CariData(self):
        print("Data operasional dicari")