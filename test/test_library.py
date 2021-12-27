import os
from pathlib import Path
from book import Book
from library import Library
import unittest

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.title = "Pan Tadeusz"
        self.firstname = "Adam"
        self.surname = "Mickiewicz"
        self.description = "Ostatni zajazd na Litwie"
        self.book = Book(self.title, self.firstname , self.surname , self.description)

    def test_add_remove_update(self):
        self.assertEqual(self.library.size(), 0)
        self.library.addBook(self.book)
        self.assertEqual(self.library.size(), 1)
        self.book2 = Book("t", "", "", "")
        self.library.addBook(self.book2)
        self.assertEqual(self.library.size(), 2)

        self.library.removeBook(self.book)
        self.assertEqual(self.library.size(), 1)
        self.library.removeBook(None)
        self.assertEqual(self.library.size(), 1)

        self.finded_book = self.library.find_book_by_title("t")

        self.assertIs(self.finded_book, self.book2)

        self.title = "Lalka"
        self.firstname = "Bolseław"
        self.surname = "Prus"
        self.description = "Historia Stanisława Wokulskiego"

        self.library.update_book_info(self.finded_book, 'title', self.title)
        self.assertEqual(self.book2.get_title(), self.title)

        self.library.update_book_info(self.finded_book, 'authors_firstname', self.firstname)
        self.assertEqual(self.book2.get_authors_firstname(), self.firstname)

        self.library.update_book_info(self.finded_book, 'authors_surname', self.surname)
        self.assertEqual(self.book2.get_authors_surname(), self.surname)

        self.library.update_book_info(self.finded_book, 'description', self.description)
        self.assertEqual(self.book2.get_description(), self.description)

        self.library.removeBook(self.book2)
        self.assertEqual(self.library.size(), 0)

        self.library.removeBook(self.book2)
        self.assertEqual(self.library.size(), 0)




    def test_get_all_books(self):
        self.book2 = Book("t", "", "", "")
        self.library.addBook(self.book)
        self.library.addBook(self.book2)
        self.assertEqual(self.library.getAllBooks(), [self.book, self.book2])
        self.assertEqual(self.library.size(), 2)
        self.library.removeBook(self.book2)
        self.library.removeBook(self.book)
        self.assertEqual(self.library.size(), 0)

    def test_import_export(self):
        _path = os.getcwd() + os.path.normpath('\\test\\test_files')
        self.library.import_books_form_csv_file(_path + os.path.normpath('\\example_lib.csv'))
        self.assertEqual(self.library.size(), 20)
        self.library.import_books_form_csv_file(_path + os.path.normpath('\\example_lib.csv'))
        self.assertEqual(self.library.size(), 20)
        self.library.export_books_to_json_file(_path + os.path.normpath('\\example_lib'))
        self.library.export_books_to_txt_file(_path + os.path.normpath('\\example_lib'))
        self.library.export_books_to_csv_file(_path + os.path.normpath('\\example_'))

        self.library = Library()
            
        self.assertEqual(self.library.size(), 0)

        
