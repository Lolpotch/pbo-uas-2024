from dashboard import Dashboard 
from barang import Barang
from transaksi import Transaksi
from operasional import Operasional
from laporan import Laporan



# Subclass dengan overriding method
class CustomDashboard(Dashboard):
    def main_menu(self):  # Overriding main_menu method
        while True:
            print("\n--- Custom Dashboard ---")
            print("1. View Data Barang")
            print("2. View Data Transaksi")
            print("3. View Data Operasional")
            print("4. View Data Laporan")
            print("5. Manage Barang")
            print("6. Manage Transaksi")
            print("7. Manage Operasional")
            print("8. Manage Laporan")
            print("9. Exit Custom Dashboard")
            choice = input("Choose an option: ")

            if choice == "1":
                self.show_data(Barang)
            elif choice == "2":
                self.show_data(Transaksi)
            elif choice == "3":
                self.show_data(Operasional)
            elif choice == "4":
                self.show_data(Laporan)
            elif choice == "5":
                self.manage_data(Barang)
            elif choice == "6":
                self.manage_data(Transaksi)
            elif choice == "7":
                self.manage_data(Operasional)
            elif choice == "8":
                self.manage_data(Laporan)
            elif choice == "9":
                print("Exiting Custom Dashboard...")
                break
            else:
                print("Invalid choice, please try again.")

