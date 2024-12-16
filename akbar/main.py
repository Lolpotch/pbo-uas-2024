from models.barang import Barang
from models.transaksi import Transaksi
from models.operasional import Operasional
from models.laporan import Laporan
from models.login import Login
from models.dashboard import Dashboard

if __name__ == "__main__":
    # Contoh implementasi
    barang = Barang(1, "Elektronik", 100, 10, 5, "2024-12-13")
    transaksi = Transaksi(1, "2024-12-13", "John Doe", "Elektronik", 2, "Lunas")
    operasional = Operasional(1, "2024-12-13", 100000, 50000, 150000)
    laporan = Laporan(1, "Jl. Sudirman", "Pengiriman sukses", "2024-12-13")
    login = Login("admin", "password")
    dashboard = Dashboard()

    # Tambahkan logika program di sini
    pass
