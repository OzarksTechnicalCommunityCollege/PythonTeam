"""
Console app entry point demonstrating the library checkout system.
Run with: python main.py
"""

from library_app.book import Book
from library_app.catalog import Catalog
from library_app.reportsSubMenu import reports_menu
from library_app.reservation import reservation_menu
from library_app.user import User
from library_app.book_status import OverdueReport

def main():
    users = {}
    statuses = []
    reservations = [] 

    catalog = Catalog()

    catalog.add_book(Book("The Pragmatic Programmer", "David Thomas", "9780135957059", 3))
    catalog.add_book(Book("Clean Code", "Robert C. Martin", "9780132350884", 2))
    catalog.add_book(Book("The DevOps Handbook", "Gene Kim", "9781942788003", 1))

    print("=== Library Management System ===")
    print()

    # Account Menu
    while True:
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter your name: ").strip()

            if name in users:
                print("Account already exists.")
            else:
                users[name] = User(name)
                print(f"Account created for {name}!")

        elif choice == "2":
            name = input("Enter your name: ").strip()

            if name not in users:
                print("Account not found.")
                continue

            current_user = users[name]
            print(f"Welcome, {current_user.name}!")
            print(f"Outstanding fines: ${current_user.fines:.2f}")
            break

        elif choice == "3":
            print("Goodbye!")
            return

        else:
            print("Invalid selection.")

        reservations = []

    while True:

        print()
        print("  Library Main Menu  ")
        print("---------------------")
        print("(1.) Checkout Book")
        print("(2.) Return Book")
        print("(3.) Manage Reservations")
        print("(4.) View Reports")
        print("(5.) View Fines")
        print("(6.) Exit")
        print("---------------------")
        choice = input("Select an option: ").strip()



        if choice == "1":
            isbn = input("Please enter the desired ISBN: ").strip()
            catalog.check_out_book(isbn, current_user)

        elif choice == "2":
            isbn = input("Enter ISBN to return: ").strip()
            catalog.return_book(isbn, current_user)

        elif choice == "3":
            reservation_menu(catalog, reservations)

        elif choice == "4":
            report = OverdueReport(statuses)
            reports_menu(report, reservations)

        elif choice == "5":
            print()
            print(f"Outstanding Fines: ${current_user.fines:.2f}")

        elif choice == "6":
            print()
            print("See you next time!")
            break
        else:
            print("Invalid input. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()