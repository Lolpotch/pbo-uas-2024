from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelss.barang import Barang
from datetime import date

class Dashboard:
    # Database setup
    DATABASE_URL = "sqlite:///my_database.db"  # Database file
    engine = create_engine(DATABASE_URL, echo=False)  # Disable query logging
    Session = sessionmaker(bind=engine)
    session = Session()

    def barang_menu():
        while True:
            print("\nBarang Menu:")
            print("1. Tambah Data")
            print("2. Edit Data")
            print("3. Hapus Data")
            print("4. Cari Data")
            print("5. Kembali")

            choice = input("Pilih opsi: ")
            if choice == "1":
                tambah_barang()
            elif choice == "2":
                edit_barang()
            elif choice == "3":
                hapus_barang()
            elif choice == "4":
                cari_barang()
            elif choice == "5":
                break
            else:
                print("Opsi tidak valid. Coba lagi.")

    def tambah_barang():
        print("\nTambah Barang:")
        jenis_barang = input("Masukkan jenis barang: ")
        stok_gudang = int(input("Masukkan stok gudang: "))
        barang_masuk = int(input("Masukkan barang masuk: "))
        barang_keluar = int(input("Masukkan barang keluar: "))
        tanggal = date.today()
        
        barang = Barang(jenis_barang=jenis_barang, stok_gudang=stok_gudang, 
                        barang_masuk=barang_masuk, barang_keluar=barang_keluar, tanggal=tanggal)
        barang.TambahData(session)

    def edit_barang():
        print("\nEdit Barang:")
        id_barang = int(input("Masukkan ID barang: "))
        barang = Barang.CariData(session, id_barang)
        if barang:
            jenis_barang = input(f"Jenis Barang ({barang.jenis_barang}): ") or barang.jenis_barang
            stok_gudang = input(f"Stok Gudang ({barang.stok_gudang}): ") or barang.stok_gudang
            barang_masuk = input(f"Barang Masuk ({barang.barang_masuk}): ") or barang.barang_masuk
            barang_keluar = input(f"Barang Keluar ({barang.barang_keluar}): ") or barang.barang_keluar
            barang.EditData(session, jenis_barang=jenis_barang, stok_gudang=int(stok_gudang),
                            barang_masuk=int(barang_masuk), barang_keluar=int(barang_keluar))
        else:
            print("Barang tidak ditemukan.")

    def hapus_barang():
        print("\nHapus Barang:")
        id_barang = int(input("Masukkan ID barang: "))
        barang = Barang.CariData(session, id_barang)
        if barang:
            confirm = input("Yakin ingin menghapus barang ini? (y/n): ")
            if confirm.lower() == "y":
                barang.HapusData(session)
            else:
                print("Penghapusan dibatalkan.")
        else:
            print("Barang tidak ditemukan.")

    def cari_barang():
        print("\nCari Barang:")
        id_barang = int(input("Masukkan ID barang: "))
        barang = Barang.CariData(session, id_barang)
        if barang:
            print(f"ID: {barang.id_barang}, Jenis: {barang.jenis_barang}, Stok: {barang.stok_gudang}, "
                f"Masuk: {barang.barang_masuk}, Keluar: {barang.barang_keluar}, Tanggal: {barang.tanggal}")
        else:
            print("Barang tidak ditemukan.")

    def main_dashboard():
        while True:
            print("\nDashboard")
            print("1. Barang")
            print("2. Transaksi")
            print("3. Laporan")
            print("4. Operasional")
            print("5. Logout")

            choice = input("Pilih opsi: ")
            if choice == "1":
                barang_menu()
            elif choice == "2":
                print("Menu Transaksi belum diimplementasikan.")
            elif choice == "3":
                print("Menu Laporan belum diimplementasikan.")
            elif choice == "4":
                print("Menu Operasional belum diimplementasikan.")
            elif choice == "5":
                print("Logout berhasil.")
                break
            else:
                print("Opsi tidak valid. Coba lagi.")