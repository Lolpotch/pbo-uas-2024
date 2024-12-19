from database import engine, Base
from database import session
from login import Login, login
from dashboard import Dashboard
from custom_dasb import CustomDashboard

# Function to create tables
def initialize_database():
    print("Initializing database...")
    Base.metadata.create_all(engine)  # Creates all tables
    print("Database initialized successfully.")

    # Run code below for first user initialization
    # Comment them if you've add the user since it'd cause error if executed twice
    # session.add(Login(username='admin', password='123'))
    # session.commit()
    # print("Admin user added successfully.")

def main():
    initialize_database() 
    while not login():
        pass

    dashboard = CustomDashboard()
    dashboard.main_menu()

if __name__ == "__main__":
    main()
