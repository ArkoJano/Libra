from lib_creator import library
from book import *

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
    print("""        |   Podaj opis: """, end="")
    description = input()
    result = int(library.addBook(Book(title, authors_firstname, authors_surname, description)))
    if title == "":
        print("""        +-------------+ Nie mozna dodac ksiazki bez tytulu! +---------------+\n""", end="")
    elif result == 1:
        print("""        +--------------------+ Dodano ksiazke do bazy! +--------------------+\n""", end="")
    elif result == -1:
        print("""        +-------------------+ Ksiazka jest juz w bazie! +-------------------+\n""", end="")
