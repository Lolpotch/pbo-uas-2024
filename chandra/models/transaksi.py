from abc import ABC
from datetime import date
from data import Data

class Transaksi(Data):
    def __init__(self, idTransaksi: int, tanggal: date, namaPelanggan: str, jenisBarang: int, jumlah: int, statBayar: str):
        self.idTransaksi = idTransaksi
        self.tanggal = tanggal
        self.namaPelanggan = namaPelanggan
        self.jenisBarang = jenisBarang
        self.jumlah = jumlah
        self.statBayar = statBayar

    def TambahData(self):
        print("Transaksi ditambahkan")

    def EditData(self):
        print("Transaksi diedit")

    def HapusData(self):
        print("Transaksi dihapus")

    def CariData(self):
        print("Transaksi dicari")