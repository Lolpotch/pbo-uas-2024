from .data import Data

class Laporan(Data):
    def __init__(self, idLaporan, AlamatKirim, Deskripsi, Tanggal):
        self.idLaporan = idLaporan
        self.AlamatKirim = AlamatKirim
        self.Deskripsi = Deskripsi
        self.Tanggal = Tanggal