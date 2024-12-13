from .data import Data

class Barang(Data):
    def __init__(self, idBarang, JenisBarang, StokGudang, BarangMasuk, BarangKeluar, Tanggal):
        self.idBarang = idBarang
        self.JenisBarang = JenisBarang
        self.StokGudang = StokGudang
        self.BarangMasuk = BarangMasuk
        self.BarangKeluar = BarangKeluar
        self.Tanggal = Tanggal