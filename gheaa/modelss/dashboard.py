from modelss.barang import Barang
from modelss.transaksi import Transaksi
from modelss.laporan import Laporan
from modelss.operasional import Operasional

class Dashboard:
    @staticmethod
    def show_menu():
        while True:
            print("\nDashboard:")
            print("1. Barang")
            print("2. Transaksi")
            print("3. Laporan")
            print("4. Operasional")
            print("5. Logout (ketik 'exit')")
            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                Dashboard.manage_data(Barang)
            elif pilihan == "2":
                Dashboard.manage_data(Transaksi)
            elif pilihan == "3":
                Dashboard.manage_data(Laporan)
            elif pilihan == "4":
                Dashboard.manage_data(Operasional)
            elif pilihan.lower() == "exit":
                print("--TERIMAKASIH--")
                break
            else:
                print("Pilihan tidak valid, coba lagi.")

    @staticmethod
    def manage_data(model):
        while True:
            print("\n1. Tambah Data")
            print("2. Edit Data")
            print("3. Hapus Data")
            print("4. Cari Data")
            print("5. Kembali")
            pilihan = input("Pilih opsi: ")

            if pilihan == "1":
                model().tambah_data()
            elif pilihan == "2":
                model().edit_data()
            elif pilihan == "3":
                model().hapus_data()
            elif pilihan == "4":
                model().cari_data()
            elif pilihan == "5":
                break
            else:
                print("Opsi tidak valid, coba lagi.")
