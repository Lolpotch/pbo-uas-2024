from abc import ABC
from datetime import date
from data import Data

class Barang(Data):
    def __init__(self, idBarang: int, JenisBarang: str, stokGudang: int, barangMasuk: int, barangKeluar: int, Tanggal: date):
        self.idBarang = idBarang
        self.JenisBarang = JenisBarang
        self.stokGudang = stokGudang
        self.barangMasuk = barangMasuk
        self.barangKeluar = barangKeluar
        self.Tanggal = Tanggal

    def TambahData(self):
        print("Barang ditambahkan")

    def EditData(self):
        print("Barang diedit")

    def HapusData(self):
        print("Barang dihapus")

    def CariData(self):
        print("Barang dicari")