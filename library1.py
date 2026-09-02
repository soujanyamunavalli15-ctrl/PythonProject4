class Library:
    def __init__(self):
        self.books = []
        self.issued_books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"'{book}' added successfully.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"'{book}' removed successfully.")
        else:
            print("Book not found.")

    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            self.issued_books.append(book)
            print(f"'{book}' issued successfully.")
        else:
            print("Book is not available.")

    def return_book(self, book):
        if book in self.issued_books:
            self.issued_books.remove(book)
            self.books.append(book)
            print(f"'{book}' returned successfully.")
        else:
            print("This book was not issued.")

    def display_books(self):
        print("\n--- Available Books ---")
        if len(self.books) == 0:
            print("No books available.")
        else:
            for i, book in enumerate(self.books, 1):
                print(i, ".", book)


# Main Program
library = Library()

while True:
    print("\n--- LIBRARY MANAGEMENT SYSTEM ---")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        library.add_book(book)

    elif choice == "2":
        book = input("Enter book name: ")
        library.remove_book(book)

    elif choice == "3":
        book = input("Enter book name: ")
        library.issue_book(book)

    elif choice == "4":
        book = input("Enter book name: ")
        library.return_book(book)

    elif choice == "5":
        library.display_books()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")