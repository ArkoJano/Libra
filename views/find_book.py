from lib_creator import library
from clear_terminal import cls

def split_string_into_chunks(string):
    """ Funkcja dzieli lancuchy znakowe na partie po 67 znakow """
    lenght_of_chunk = 67
    chunks = [string[i:i+lenght_of_chunk] for i in range(0, len(string), lenght_of_chunk)]
    return chunks


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
            option = 0
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