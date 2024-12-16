from datetime import date
from modelss.data import Data

class Transaksi(Data):
    def __init__(self, id_transaksi: int, tanggal: date, nama_pelanggan: str, jenis_barang: int, jumlah: int, stat_bayar: str):
        self.id_transaksi = id_transaksi
        self.tanggal = tanggal
        self.nama_pelanggan = nama_pelanggan
        self.jenis_barang = jenis_barang
        self.jumlah = jumlah
        self.stat_bayar = stat_bayar

    def TambahData(self):
        print("Transaksi ditambahkan")

    def EditData(self):
        print("Transaksi diedit")

    def HapusData(self):
        print("Transaksi dihapus")

    def CariData(self):
        print("Transaksi dicari")