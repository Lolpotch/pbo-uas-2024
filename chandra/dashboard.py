from sqlalchemy.types import Integer, Date
from datetime import datetime
from database import session
from barang import Barang
from transaksi import Transaksi
from operasional import Operasional
from laporan import Laporan

class Dashboard:
    def __init__(self):
        self.session = session

    def show_data(self, model):
        print(f"--- Data {model.__tablename__.capitalize()} ---")
        data = self.session.query(model).all()
        if not data:
            print("No data available.")
            return

        for row in data:
            print(" | ".join(f"{key}: {value}" for key, value in row.__dict__.items() if key != '_sa_instance_state'))

    def edit_data(self, model):
        print(f"--- Edit Data in {model.__tablename__.capitalize()} ---")
        model.edit_data(self, model)

    def delete_data(self, model):
        print(f"--- Delete Data in {model.__tablename__.capitalize()} ---")
        model.delete_data(self, model)
        
    def manage_data(self, model):
        while True:
            print(f"\nManage {model.__tablename__.capitalize()}:")
            print("1. Add Data")
            print("2. Edit Data")
            print("3. Delete Data")
            print("4. Search Data")
            print("5. Back to Dashboard")
            choice = input("Choose an option: ")

            if choice == "1":
                model.add_data(self)
            elif choice == "2":
                self.edit_data(model)
            elif choice == "3":
                self.delete_data(model)
            elif choice == "4":
                model.search_data(self)
            elif choice == "5":
                break
            else:
                print("Invalid choice, please try again.")

    def main_menu(self):
        while True:
            print("\n--- Dashboard ---")
            print("1. Show Data Barang")
            print("2. Show Data Transaksi")
            print("3. Show Data Operasional")
            print("4. Show Data Laporan")
            print("5. Manage Barang")
            print("6. Manage Transaksi")
            print("7. Manage Operasional")
            print("8. Manage Laporan")
            print("9. Logout")
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
                print("Logging out...")
                break
            else:
                print("Invalid choice, please try again.")
