from book import *
from library import *
import csv
import os

library = Library()


library.import_books_form_csv_file("example_lib.csv")
# csv_file.close()
# library.printAllBooks()

# library.export_books_to_csv_file("exported.csv")

def go_on():
    """ Funkcja zatrzymuje dzialanie programu czekajac na dzialanie uzytkownika """

    input("""        |   Nacisnij enter klawisz aby kontynuowac...                       |
        +-------------------------------------------------------------------+""")

def split_string_into_chunks(string):
    """ Funkcja dzieli lancuchy znakowe na partie po 67 znakow """
    lenght_of_chunk = 67
    chunks = [string[i:i+lenght_of_chunk] for i in range(0, len(string), lenght_of_chunk)]
    return chunks


def print_main_menu():
    """ Funkcja wyswietla glowne menu programu """

    print(
        """\r
        +----------------------------+ Libra +------------------------------+
        |   1. Dodaj ksiazke                                                |
        |   2. Usun ksiazke                                                 |
        |   3. Wyszukaj ksiazke w bibliotece                                |
        |   4. Wyswietl liste wszystkich ksiazek                            |
        |   5. Importuj bilioteke z pliku                                   |
        |   6. Eksportuj biblioteke do pliku                                |
        |   7. Wyjdz                                                        |
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
    print("""        |   Podaj opis: """, end="")
    description = input()
    result = int(library.addBook(Book(title, authors_firstname, authors_surname, description)))
    if title == "":
        print("""        +-------------+ Nie mozna dodac ksiazki bez tytulu! +---------------+\n""", end="")
    elif result == 1:
        print("""        +--------------------+ Dodano ksiazke do bazy! +--------------------+\n""", end="")
    elif result == -1:
        print("""        +-------------------+ Ksiazka jest juz w bazie! +-------------------+\n""", end="")


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
        main()
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
    if full_lib == []:
        print(f"        | Brak ksiazek do wyswietlenia                                      |")

    for book in full_lib:
        print(f"        |{book.get_ID():^6}|{book.get_title():<28}|{book.get_author():<31}|")
        
    print("""        +-------------------------------------------------------------------+\n""", end="")

def print_find_book_menu():
    print("""
        +-----------------------+ Wyszukaj ksiazke +------------------------+
        """
            , end="")

    title = input("""|   Podaj tytul: """)
    print("\r        +-------------------------------------------------------------------+")
    book = library.find_book_by_title(title)
    
    cls()
    if book != None:
        option = 0
        while(option != 8):
            cls()
            print(
        """\r
        +-------------------------------------------------------------------+
        |  ID  |           Tytul            |             Autor             |
        +-------------------------------------------------------------------+"""
            )
            print(f"        |{book.get_ID():^6}|{book.get_title():<28}|{book.get_author():<31}|", end="")
            print(
            """
        +--- Opis ----------------------------------------------------------+""")
            description = book.get_description()
            if type(description) == type(list()):
                description_string = ""
                for i in description:
                    description_string += str(i)
            if len(description_string) > 67:
                description_string = split_string_into_chunks(description_string)
                for i in range(len(description_string)):
                    if i != len(description_string)-1:
                        print(f"        |{description_string[i]:<67}|")
                    else:
                        print(f"        |{description_string[i]:<67}|", end="")

            else:
                print(f"        |{description_string:<67}|")
        
            print(
        """\r
        +-------------------------------------------------------------------+
        | 1. Edytuj dane ksiązki | 2. Usun ksiazke z bazy | 7. Wyjdź do menu|
        +-------------------------------------------------------------------+
        """, end="")
            try:
                option = int(input("|   Opcja: "))
            except ValueError:
                print("""        +-------------------------------------------------------------------+
        |   Niepoprawna wartosc!                                              |""")

            if option == 1:
                print_update_book_menu(book)
            elif option == 2:
                library.removeBook(book)
                print("""        +--------------------+ Usunieto ksiazke z bazy! +-------------------+\n""", end="")
                break
            elif option == 7:
                break
            else:
                print("""        +-------------------------------------------------------------------+
        |   Niepoprawna wartosc!                                              |""")

        print("\r        +-------------------------------------------------------------------+")

    
    else:
        print(
        """\r
        +-------------------------------------------------------------------+
        |  Nie ksiązki o podanym tytule                                     |
        +-------------------------------------------------------------------+"""
        )

def print_update_book_menu(book):
    print("""
        +----------------------+ Edytuj dane ksiazki +----------------------+
        |   1. Tytul                                                        |
        |   2. Imie autora                                                  |
        |   3. Nazwisko autora                                              | 
        |   4. Opis                                                         |
        |   5. Wroc                                                         |
        +-------------------------------------------------------------------+
        """
        , end="\r", flush=True)
    option = 0
    try:
        option = int(input("        |   Co chcesz zedytowac?:  "))
    except ValueError:
        print("""        +-------------------------------------------------------------------+
        |   Niepoprawna wartosc!                                              |""")

    if option == 0:
        print("""        +-------------------------------------------------------------------+
        |   Niepoprawna wartosc!                                              |""")
    elif option == 1:
        new_title = input("        |   Podaj nowy tytuł: ")
        library.update_book_info(book, "title", new_title)
    elif option == 2:
        new_authors_firstname = input("        |   Podaj nowe imię: ")
        library.update_book_info(book, "authors_firstname", new_authors_firstname)
    elif option == 3:
        new_authors_surname = input("        |   Podaj nowe nazwisko: ")
        library.update_book_info(book, "authors_surname", new_authors_surname)
    elif option == 4:
        new_description = input("        |   Podaj nowy opis: ")
        library.update_book_info(book, "description", new_description)
    else:
        print("        |   Niepoprawna opcja!")  
        
def print_export_books_menu():
    print("""
        +--------------------+ Eksportuj dane do pliku +--------------------+"""
    )
    try:
        file_name = input("        |   Podaj nazwe pliku (bez rozszerzenia): ")
    except ValueError:
        print("Niepoprawna wartosc!")
    cls()
    print("""
        +-------------------+ Podaj rozszerzenie pliku +--------------------+
        |   1. .CSV                                                         |
        |   2. .JSON                                                        |
        |   3. .txt                                                         | 
        +-------------------------------------------------------------------+
        """
        , end="\r", flush=True)
    try:
        option = int(input("        |   Opcja: "))
    except ValueError:
        print("Niepoprawna wartosc!")
    if option == 1:
        counter = library.export_books_to_csv_file(file_name)
        print(
        f"""\r
        +-------------------------------------------------------------------+
        |  Ilosc eksportowanych ksiazek: {counter:<16}                   |
        +-------------------------------------------------------------------+"""
        )
    elif option == 2: 
        counter = library.export_books_to_json_file(file_name)
        print(
        f"""\r
        +-------------------------------------------------------------------+
        |  Ilosc eksportowanych ksiazek: {counter:<16}                   |
        +-------------------------------------------------------------------+"""
        )
    elif option == 3: 
        counter = library.export_books_to_txt_file(file_name)
        print(
        f"""\r
        +-------------------------------------------------------------------+
        |  Ilosc eksportowanych ksiazek: {counter:<16}                   |
        +-------------------------------------------------------------------+"""
        )
    else:
        print("        |   Niepoprawna opcja!") 


def print_import_books_menu():
    print("""
        +---------------------+ Importuj dane z pliku +---------------------+"""
    )
    try:
        file_name = input("        |   Podaj nazwe pliku (z rozszerzeniem): ")
    except ValueError:
        print("Niepoprawna wartosc!")
    cls()
    
    file_extension = file_name.split(".")[-1]

    if file_extension == "csv":
        
        try:
            counter = library.import_books_form_csv_file(file_name)
            print(
        f"""\r
        +-------------------------------------------------------------------+
        |  Ilosc importowanych ksiazek: {counter:<16}                    |
        +-------------------------------------------------------------------+"""
        )
        except FileNotFoundError:
            print("        |   Nieznaleziono takiego pliku!") 
    elif file_extension == "json":
        try:
            counter = library.import_books_from_json_file(file_name)
            print(
        f"""\r
        +-------------------------------------------------------------------+
        |  Ilosc importowanych ksiazek: {counter:<16}                    |
        +-------------------------------------------------------------------+"""
        )
        except FileNotFoundError:
            print("        |   Nieznaleziono takiego pliku!")
    else:
        print("""        +---------------------+ Importuj dane z pliku +---------------------+
        |   Niepoprawne rozszerzenie!                                      |""") 

def choose_option(option):
    """ Funkcja odpowiadajaca za wybor opcji z menu glownego """

    cls()
    if option == 1:
        print_add_book_menu()
    elif option == 2:
        print_delete_book_menu()
    elif option == 3:
        print_find_book_menu()
    elif option == 4:
        print_all_books()
    elif option == 5:
        print_import_books_menu()
    elif option == 6:
        print_export_books_menu()
    elif option == 7:
        exit()
    else:
        print("        |   Niepoprawna opcja!") 

def cls():
    """ Funkcja czyszczaca caly terminal """
    os.system('cls' if os.name=='nt' else 'clear')

def main():
    while True:
        cls()
        print_main_menu()
        try:
            option = int(input("        |   Opcja: "))
        except ValueError:
            print("Niepoprawna wartosc!")
            continue
        choose_option(option)
        go_on()

main()