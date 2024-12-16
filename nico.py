import datetime

# Class Login
class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def validate_login(self):
        # Simulasi validasi login (bisa diubah sesuai kebutuhan)
        return self.username == "admin" and self.password == "1234"

# Class Barang
class Barang:
    def __init__(self, id_barang, jenis_barang, stok_gudang, barang_masuk, barang_keluar, tanggal):
        self.id_barang = id_barang
        self.jenis_barang = jenis_barang
        self.stok_gudang = stok_gudang
        self.barang_masuk = barang_masuk
        self.barang_keluar = barang_keluar
        self.tanggal = tanggal

# Class Transaksi
class Transaksi:
    def __init__(self, id_transaksi, tanggal, nama_pelanggan, jenis_barang, jumlah, status_bayar):
        self.id_transaksi = id_transaksi
        self.tanggal = tanggal
        self.nama_pelanggan = nama_pelanggan
        self.jenis_barang = jenis_barang
        self.jumlah = jumlah
        self.status_bayar = status_bayar

# Class Operasional
class Operasional:
    def __init__(self, id_operasional, tanggal, biaya_supir, total_bayar):
        self.id_operasional = id_operasional
        self.tanggal = tanggal
        self.biaya_supir = biaya_supir
        self.total_bayar = total_bayar

# Class Laporan
class Laporan:
    def __init__(self, id_laporan, aktivitas, deskripsi, tanggal):
        self.id_laporan = id_laporan
        self.aktivitas = aktivitas
        self.deskripsi = deskripsi
        self.tanggal = tanggal

# Main Program
def main():
    print("===== SISTEM INPUT DATA =====")

    # Login
    print("\nLogin System")
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")
    user = Login(username, password)
    if user.validate_login():
        print("Login Berhasil!\n")
    else:
        print("Login Gagal! Program berhenti.")
        return

    # Input Barang
    print("\nInput Data Barang")
    id_barang = int(input("ID Barang: "))
    jenis_barang = input("Jenis Barang: ")
    stok_gudang = int(input("Stok Gudang: "))
    barang_masuk = int(input("Barang Masuk: "))
    barang_keluar = int(input("Barang Keluar: "))
    tanggal_barang = datetime.date.today()
    barang = Barang(id_barang, jenis_barang, stok_gudang, barang_masuk, barang_keluar, tanggal_barang)

    # Input Transaksi
    print("\nInput Data Transaksi")
    id_transaksi = int(input("ID Transaksi: "))
    tanggal_transaksi = datetime.date.today()
    nama_pelanggan = input("Nama Pelanggan: ")
    jenis_barang_transaksi = input("Jenis Barang: ")
    jumlah = int(input("Jumlah: "))
    status_bayar = input("Status Bayar (Lunas/Belum): ")
    transaksi = Transaksi(id_transaksi, tanggal_transaksi, nama_pelanggan, jenis_barang_transaksi, jumlah, status_bayar)

    # Input Operasional
    print("\nInput Data Operasional")
    id_operasional = int(input("ID Operasional: "))
    tanggal_operasional = datetime.date.today()
    biaya_supir = int(input("Biaya Supir: "))
    total_bayar = int(input("Total Bayar: "))
    operasional = Operasional(id_operasional, tanggal_operasional, biaya_supir, total_bayar)

    # Input Laporan
    print("\nInput Data Laporan")
    id_laporan = int(input("ID Laporan: "))
    aktivitas = input("Aktivitas: ")
    deskripsi = input("Deskripsi: ")
    tanggal_laporan = datetime.date.today()
    laporan = Laporan(id_laporan, aktivitas, deskripsi, tanggal_laporan)

    # Menampilkan Ringkasan Data
    print("\n===== RINGKASAN DATA =====")
    print(f"Barang - ID: {barang.id_barang}, Jenis: {barang.jenis_barang}, Stok: {barang.stok_gudang}, Masuk: {barang.barang_masuk}, Keluar: {barang.barang_keluar}, Tanggal: {barang.tanggal}")
    print(f"Transaksi - ID: {transaksi.id_transaksi}, Tanggal: {transaksi.tanggal}, Pelanggan: {transaksi.nama_pelanggan}, Jenis Barang: {transaksi.jenis_barang}, Jumlah: {transaksi.jumlah}, Status: {transaksi.status_bayar}")
    print(f"Operasional - ID: {operasional.id_operasional}, Tanggal: {operasional.tanggal}, Biaya Supir: {operasional.biaya_supir}, Total Bayar: {operasional.total_bayar}")
    print(f"Laporan - ID: {laporan.id_laporan}, Aktivitas: {laporan.aktivitas}, Deskripsi: {laporan.deskripsi}, Tanggal: {laporan.tanggal}")

if __name__ == "__main__":
    main()
