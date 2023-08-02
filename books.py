import openpyxl
import sys
import time
import requests 

def check_item_in_database(name, csv_location):
    url = 'http://127.0.0.1:5000/'  # Replace with the correct URL of your microservice
    data = {
        "name": name,
        "csv_location": csv_location
    }

    response = requests.post(url, json=data)

    if response.text == "False":
        print(f"The item '{name}' does not exist in the database.")
    else:
        print(f"The item '{name}' exists in the database.")

class Book:
    def __init__(self, title, author, genre, year):
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year

class BookCatalog:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def delete_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return True
        return False

    def search_books(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def list_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Year: {book.year}")

    def save_to_excel(self, file_path):
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active

        for book in self.books:
            sheet.append([book.title, book.author, book.genre, book.year])

        workbook.save(file_path)


def main():
    menu = """Please select from the following options:
    1. Add book
    2. Delete book
    3. Search books
    4. See a list of all books
    5. Save book to Excel
    6. Quit

    Your selection: """
    welcome = "Welcome to your book catalog!"

    print(welcome)

    excel_file = "/Users/julieweber/Documents/Books/book_list.xlsx"
    book_catalog = BookCatalog()  # Create an instance of BookCatalog

    while (user_input := input(menu)) != "6":
        if user_input == "1":
            title = input("Enter the book title: ")
            author = input("Enter the author's name: ")
            genre = input("Enter the genre: ")
            year = input("Enter the publication year: ")
            book = Book(title, author, genre, year)
            book_catalog.add_book(book)
            print("Adding...")
        elif user_input == "2":
            title = input("Enter the book title to delete: ")
            if book_catalog.delete_book(title):
                print("Book deleted successfully.")
            else:
                print("Book not found.")
        elif user_input == "3":
            name = input("Enter the book name to search: ")
            csv_file_location = "/Users/julieweber/Documents/Books/book_list.xlsx"  # Replace with the correct CSV file path
            check_item_in_database(name, csv_file_location)
            if book:
                print(f"Book found: {book.title}, {book.author}, {book.genre}, {book.year}")
            else:
                print("Book not found.")
        elif user_input == "4":
            book_catalog.list_books()
        elif user_input == "5":
            book_catalog.save_to_excel(excel_file)
            print(f"Book catalog saved to '{excel_file}'.")
            time.sleep(2)  # Add a 2-second delay
            sys.exit()  # Properly exit the program
        else:
            print("Invalid input. Please try again.")

    # Save the book catalog before quitting
    book_catalog.save_to_excel(excel_file)
    print(f"Book catalog saved to '{excel_file}'.")

    print("Exiting...")
    sys.exit()  # Properly exit the program

if __name__ == "__main__":
    main()


