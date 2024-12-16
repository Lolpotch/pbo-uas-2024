class Login:
    @staticmethod
    def login():
        print("\nSELAMAT DATANG DI SISTEM MANAJEMEN INVENTORI DAN PENJUALAN PT INHUTANI V")
        while True:
            username = input("\nUser: ")
            password = input("Password: ")
            if username == "admin" and password == "admin":
                print("Login berhasil!")
                break
            else:
                print("Login gagal! Silakan coba lagi.")