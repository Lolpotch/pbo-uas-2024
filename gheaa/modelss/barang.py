from modelss.data import Data

class Barang(Data):
    def __init__(self, nama_barang, stok_gudang, harga):
        self.nama_barang = nama_barang
        self.stok_gudang = stok_gudang
        self.harga = harga

    def tambah_data(self):
        print(f"Menambahkan Barang: {self.nama_barang}, Stok: {self.stok_gudang}, Harga: {self.harga}")

    def edit_data(self, nama_barang, stok_gudang, harga):
        self.nama_barang = nama_barang
        self.stok_gudang = stok_gudang
        self.harga = harga
        print("Data barang berhasil diperbarui.")

    def hapus_data(self):
        print(f"Data barang '{self.nama_barang}' berhasil dihapus.")

    def cari_data(self):
        print(f"Mencari data barang: {self.nama_barang}")
