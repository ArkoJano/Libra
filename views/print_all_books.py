from lib_creator import library


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
