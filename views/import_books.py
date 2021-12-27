from lib_creator import library
from clear_terminal import cls

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
