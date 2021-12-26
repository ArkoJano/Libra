from book import *
from library import *
import csv
import os

library = Library()
# book = Book("Pan Tadeusz", "Adam", "Mickiewicz")

# library.printAllBooks()
# library.addBook(book)
# library.printAllBooks()
# print(library.find_book_by_title(book.get_title()))
# library.removeBook(book)
# library.printAllBooks()

csv_file = open('example_lib.csv')
library.import_books_form_csv_file(csv_file)
csv_file.close()
# library.printAllBooks()

library.export_books_to_csv_file("exported.csv")

def go_on():
    """ Funkcja zatrzymuje dzialanie programu czekajac na dzialanie uzytkownika """

    input("""        |   Nacisnij enter klawisz alby kontynuowac...                      |
        +-------------------------------------------------------------------+""")

def print_main_menu():
    """ Funkcja wyswietla glowne menu programu """

    print(
        """\r
        +----------------------------+ Libra +------------------------------+
        |   1. Dodaj ksiazke                                                |
        |   2. Usun ksiazke                                                 |
        |   3. Wyszukaj ksiazke w bibliotece                                |
        |   4. Wyswietl liste wszystkich ksiazek                            |
        |   5. Zaktualizuj dane ksiazki                                     |
        |   6. Importuj bilioteke                                           |
        |   7. Eksportuj do pliku                                           |
        |   8. Wyjdz                                                        |
        +-------------------------------------------------------------------+
        """
        , end="\r", flush=True)

def print_add_book_menu():
    """ Funkcja wyswietlajaca menu dodawania ksiazki do bazydanych """

    print("""
        +-------------------------+ Dodaj ksiazke +-------------------------+
        |   Podaj tytul: """, end="", flush=True)
    title = input()
    print("""        |   Podaj imie autora: """, end="", flush=True)
    authors_firstname = input()    
    print("""        |   Podaj nazwisko autora: """, end="")
    authors_surname = input()
    library.addBook(Book(title, authors_firstname, authors_surname))
    print("""        +--------------------+ Dodano ksiazke do bazy! +--------------------+\n""", end="")


def print_delete_book_menu():
    """ Funkcja wyswietlajaca menu dodawania ksiazki do bazydanych """

    print("""
        +-------------------------+ Usun ksiazke +--------------------------+
        |   1. Wybierz ksiazke po tytule                                    |
        |   2. Wyswietl liste i wybierz po ID                               |
        +-------------------------------------------------------------------+
        """
        , end="\r", flush=True)
    option = int(input("        |   Opcja: "))

    if option == 1:
        title = input("""        |   Podaj tytul: """)
        book = library.find_book_by_title(title)
        print(book)
        library.removeBook(book)
        print("""        +--------------------+ Usunieto ksiazke z bazy! +-------------------+\n""", end="")
    elif option == 2:
        print_all_books()
        ID = input("""        |   Wybierz ID: """)
        book = library.find_book_by_ID(ID)
        library.removeBook(book)
        print("""        +--------------------+ Usunieto ksiazke z bazy! +-------------------+\n""", end="")
    else:
        print("        |   Niepoprawna opcja! ")


    
def print_all_books():
    """ Funkcja wypisujaca wszystkie ksiazki w bazie danych """

    print(
        """\r
        +----------------------------+ Libra +------------------------------+
        |  ID  |           Tytul            |             Autor             |
        +-------------------------------------------------------------------+"""
        )
    full_lib = library.getAllBooks()
    for book in full_lib:
        print(f"        |{book.get_ID():^6}|{book.get_title():<28}|{book.get_author():<31}|")
        
    print("""        +-------------------------------------------------------------------+\n""", end="")

def choose_option(option):
    """ Funkcja odpowiadajaca za wybor opcji z menu glownego """

    cls()
    if option == 1:
        print_add_book_menu()
    elif option == 2:
        print_delete_book_menu()
    elif option == 4:
        print_all_books()
    elif option == 8:
        exit()

def cls():
    """ Funkcja czyszczaca caly terminal """
    os.system('cls' if os.name=='nt' else 'clear')

while True:
    cls()
    print_main_menu()
    option = int(input("        |   Opcja: "))
    choose_option(option)
    go_on()
