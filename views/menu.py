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