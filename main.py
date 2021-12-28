from book import *
from library import *
from lib_creator import library
from clear_terminal import cls
from views.menu import print_main_menu
from views.add_book import print_add_book_menu
from views.remove_book import print_delete_book_menu
from views.print_all_books import print_all_books
from views.find_book import print_find_book_menu
from views.export_books import print_export_books_menu 
from views.import_books import print_import_books_menu 
from goon import go_on


# library.import_books_form_csv_file("example_lib.csv")



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



def main():

    """ Funkcja odpowiadajaca za cala dzialanie calego programu """


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

# main()