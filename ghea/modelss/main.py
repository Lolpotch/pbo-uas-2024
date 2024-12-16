from login import Login
from barang import BarangOperations
from transaksi import TransaksiOperations
from operasional import OperasionalOperations
from laporan import LaporanOperations
from datetime import datetime

def main():
    login = Login()
    barang_ops = BarangOperations()
    transaksi_ops = TransaksiOperations()
    operasional_ops = OperasionalOperations()
    laporan_ops = LaporanOperations()

    print("Selamat datang di Sistem Manajemen Inventori dan Penjualan")

    # Login
    while True:
        try:
            username = input("Masukkan Username: ")
            password = input("Masukkan Password: ")
            if login.validasi_data(username, password):
                print("Login berhasil!\n")
                break
            else:
                raise ValueError("Username atau Password salah!")
        except ValueError as e:
            print(e)

    # Menu Utama
    while True:
        print("1. Halaman Barang")
        print("2. Halaman Transaksi")
        print("3. Halaman Operasional")
        print("4. Halaman Laporan")
        print("5. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            id_barang = input("ID Barang: ")
            jenis_barang = input("Jenis Barang: ")
            stok = input("Stok Gudang: ")
            masuk = input("Barang Masuk: ")
            keluar = input("Barang Keluar: ")
            tanggal = input("Tanggal (YYYY-MM-DD): ")
            print(barang_ops.tambah_data(id_barang, jenis_barang, stok, masuk, keluar, datetime.strptime(tanggal, "%Y-%m-%d")))

        elif pilihan == "2":
            id_transaksi = input("ID Transaksi: ")
            tanggal = input("Tanggal (YYYY-MM-DD): ")
            pelanggan = input("Nama Pelanggan: ")
            jenis_barang = input("Jenis Barang: ")
            jumlah = input("Jumlah: ")
            status = input("Status Bayar (Lunas/Belum): ")
            print(transaksi_ops.tambah_data(id_transaksi, datetime.strptime(tanggal, "%Y-%m-%d"), pelanggan, jenis_barang, jumlah, status))

        elif pilihan == "3":
            id_transaksi = input("ID Transaksi: ")
            tanggal = input("Tanggal (YYYY-MM-DD): ")
            biaya_mobil = input("Biaya Mobil: ")
            biaya_supir = input("Biaya Supir: ")
            print(operasional_ops.tambah_data(id_transaksi, datetime.strptime(tanggal, "%Y-%m-%d"), biaya_mobil, biaya_supir))

        elif pilihan == "4":
            id_laporan = input("ID Laporan: ")
            alamat = input("Alamat Kirim: ")
            deskripsi = input("Deskripsi: ")
            tanggal = input("Tanggal (YYYY-MM-DD): ")
            print(laporan_ops.tambah_data(id_laporan, alamat, deskripsi, datetime.strptime(tanggal, "%Y-%m-%d")))

        elif pilihan == "5":
            print("Terima kasih! Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid! Coba lagi.\n")

if __name__ == "__main__":
    main()
