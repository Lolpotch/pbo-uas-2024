from datetime import date
from modelss.data import Data

class Operasional(Data):
    def __init__(self, id_transaksi: int, tanggal: date, biaya_mobil: int, biaya_supir: int, total_biaya: int):
        self.id_transaksi = id_transaksi
        self.tanggal = tanggal
        self.biaya_mobil = biaya_mobil
        self.biaya_supir = biaya_supir
        self.total_biaya = total_biaya

    def TambahData(self):
        print("Data operasional ditambahkan")

    def EditData(self):
        print("Data operasional diedit")

    def HapusData(self):
        print("Data operasional dihapus")

    def CariData(self):
        print("Data operasional dicari")