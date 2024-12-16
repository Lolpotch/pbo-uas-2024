from modelss.data import Data

class Transaksi(Data):
    def __init__(self, nama_pelanggan, jenis_barang, jumlah, status_bayar):
        self.nama_pelanggan = nama_pelanggan
        self.jenis_barang = jenis_barang
        self.jumlah = jumlah
        self.status_bayar = status_bayar

    def tambah_data(self):
        print(f"Menambahkan Transaksi: Pelanggan: {self.nama_pelanggan}, Barang: {self.jenis_barang}, Jumlah: {self.jumlah}, Status: {self.status_bayar}")

    def edit_data(self, nama_pelanggan, jenis_barang, jumlah, status_bayar):
        self.nama_pelanggan = nama_pelanggan
        self.jenis_barang = jenis_barang
        self.jumlah = jumlah
        self.status_bayar = status_bayar
        print("Data transaksi berhasil diperbarui.")

    def hapus_data(self):
        print(f"Data transaksi '{self.nama_pelanggan}' berhasil dihapus.")

    def cari_data(self):
        print(f"Mencari data transaksi pelanggan: {self.nama_pelanggan}")
