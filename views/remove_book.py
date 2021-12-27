from lib_creator import library
from views.menu import *
from book import *
from clear_terminal import cls
from goon import go_on
from views.print_all_books import *

def print_delete_book_menu():
    """ Funkcja wyswietlajaca menu dodawania ksiazki do bazydanych """

    print("""
        +-------------------------+ Usun ksiazke +--------------------------+
        |   1. Wybierz ksiazke po tytule                                    |
        |   2. Wyswietl liste i wybierz po ID                               |
        |   3. Wroc do menu                                                 |
        +-------------------------------------------------------------------+
        """
        , end="\r", flush=True)
    option = 0
    try:
        option = int(input("        |   Opcja: "))
    except ValueError:
        print("Niepoprawna wartosc!")
    cls()
    if option == 0:
        print("""        +-------------------------------------------------------------------+
        | Niepoprawna wartosc!                                              |""")
    elif option == 1:
        print("""
        +-------------------------+ Usun ksiazke +--------------------------+""")
        title = input("""        |   Podaj tytul: """)
        book = library.find_book_by_title(title)
        if book != None:
            library.removeBook(book)
            print("""        +--------------------+ Usunieto ksiazke z bazy! +-------------------+\n""", end="")
        else:
            cls()  
            print("""        +-------------------------------------------------------------------+
        | Nie ma takiej ksiazki w bazie!                                    |   
        +-------------------------------------------------------------------+\n""", end="")    
    elif option == 2:
        print_all_books()
        ID = input("""        |   Wybierz ID: """)
        book = library.find_book_by_ID(ID)
        if book != None:
            library.removeBook(book)
            print("""        +--------------------+ Usunieto ksiazke z bazy! +-------------------+\n""", end="")
        else:
            cls()
            print("""        +-------------------------------------------------------------------+
        | Nie ma takiej ksiazki w bazie!                                    |   
        +-------------------------------------------------------------------+\n""", end="")
    elif option == 3:
        pass
    else:
        print("        |   Niepoprawna opcja! ")
