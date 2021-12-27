from lib_creator import library
from clear_terminal import cls

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
