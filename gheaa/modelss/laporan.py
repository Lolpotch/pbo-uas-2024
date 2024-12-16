from modelss.data import Data

class Laporan(Data):
    def __init__(self, deskripsi):
        self.deskripsi = deskripsi

    def tambah_data(self):
        print(f"Menambahkan Laporan: {self.deskripsi}")

    def edit_data(self, deskripsi):
        self.deskripsi = deskripsi
        print("Data laporan berhasil diperbarui.")

    def hapus_data(self):
        print(f"Data laporan '{self.deskripsi}' berhasil dihapus.")

    def cari_data(self):
        print(f"Mencari laporan: {self.deskripsi}")