from .data import Data

class Operasional(Data):
    def __init__(self, idTransaksi, Tanggal, BiayaMobil, BiayaSupir, TotalBiaya):
        self.idTransaksi = idTransaksi
        self.Tanggal = Tanggal
        self.BiayaMobil = BiayaMobil
        self.BiayaSupir = BiayaSupir
        self.TotalBiaya = TotalBiaya