from book import *
from library import *
import csv
import sys

library = Library()
book = Book("Pan Tadeusz", "Adam", "Mickiewicz")

# library.printAllBooks()
# library.addBook(book)
# library.printAllBooks()
# print(library.find_book_by_title(book.get_title()))
# library.removeBook(book)
# library.printAllBooks()

csv_file = open('example_lib.csv')
library.import_books_form_csv_file(csv_file)
csv_file.close()
library.printAllBooks()

library.export_books_to_csv_file("exported.csv")

def print_main_menu():
    print(
        """\r
        +--------------------+ Libra +--------------------+
        |   1. Dodaj książkę                              |
        |   2. Usuń książkę                               |
        |   3. Wyszukaj książkę w bibliotece              |
        |   4. Wyświetl listę wszystkich książek          |
        |   5. Zaktualizuj dane książki                   |
        |   6. Importuj biliotekę                         |
        |   7. Eksportuj do pliku                         |
        +-------------------------------------------------+
        """
        , end="\r", flush=True)

def print_add_book_menu():
    print("""\r
        +--------------------+ Libra +--------------------+
        |   Podaj tytuł: """, end="", flush=True)
    title = input()
    print("""        |   Podaj imie autora: """, end="", flush=True)
    authors_firstname = input()    
    print("""        |   Podaj nazwisko autora: """, end="")
    authors_surname = input()
    

def choose_option(option):
    options = {
        1:print_add_book_menu()
    }

while True:
    print_main_menu()
    option = input("Opcje: ")
    choose_option(option)
