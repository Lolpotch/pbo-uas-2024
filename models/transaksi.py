from .data import Data

class Transaksi(Data):
    def __init__(self, idTransaksi, Tanggal, NamaPelanggan, JenisBarang, Jumlah, StatusBayar):
        self.idTransaksi = idTransaksi
        self.Tanggal = Tanggal
        self.NamaPelanggan = NamaPelanggan
        self.JenisBarang = JenisBarang
        self.Jumlah = Jumlah
        self.StatusBayar = StatusBayar