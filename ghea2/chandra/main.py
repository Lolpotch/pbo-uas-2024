from login import login
from dashboard import Dashboard

def main():
    while not login():
        pass

    dashboard = Dashboard()
    dashboard.main_menu()

if __name__ == "__main__":
    main()