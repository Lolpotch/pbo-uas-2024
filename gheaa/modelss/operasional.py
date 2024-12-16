from modelss.data import Data

class Operasional(Data):
    def __init__(self, biaya_mobil, biaya_supir):
        self.biaya_mobil = biaya_mobil
        self.biaya_supir = biaya_supir
        self.total_biaya = biaya_mobil + biaya_supir

    def tambah_data(self):
        print(f"Menambahkan Operasional: Biaya Mobil: {self.biaya_mobil}, Biaya Supir: {self.biaya_supir}, Total: {self.total_biaya}")

    def edit_data(self, biaya_mobil, biaya_supir):
        self.biaya_mobil = biaya_mobil
        self.biaya_supir = biaya_supir
        self.total_biaya = biaya_mobil + biaya_supir
        print("Data operasional berhasil diperbarui.")

    def hapus_data(self):
        print(f"Data operasional dengan total biaya {self.total_biaya} berhasil dihapus.")

    def cari_data(self):
        print(f"Mencari data operasional dengan total biaya: {self.total_biaya}")