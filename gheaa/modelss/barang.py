from datetime import date
from modelss.data import Data

class Barang(Data):
    def __init__(self, id_barang: int, jenis_barang: str, stok_gudang: int, barang_masuk: int, barang_keluar: int, tanggal: date):
        self.id_barang = id_barang
        self.jenis_barang = jenis_barang
        self.stok_gudang = stok_gudang
        self.barang_masuk = barang_masuk
        self.barang_keluar = barang_keluar
        self.tanggal = tanggal

    def TambahData(self):
        print("Barang ditambahkan")

    def EditData(self):
        print("Barang diedit")

    def HapusData(self):
        print("Barang dihapus")

    def CariData(self):
        print("Barang dicari")
