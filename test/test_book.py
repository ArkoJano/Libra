from book import Book
import unittest

class TestBook(unittest.TestCase):

    def setUp(self):
        self.title = "Pan Tadeusz"
        self.firstname = "Adam"
        self.surname = "Mickiewicz"
        self.description = "Ostatni zajazd na Litwie"
        self.book = Book(self.title, self.firstname , self.surname , self.description)

    def test_constructor(self):
        with self.assertRaises(ValueError):
            self.book = Book("","","","")
            book = Book("s","s","s",1)
            book = Book("s","s","s","s")
    

    def test_get_methods(self):
        
        
        self.assertEqual(self.book.get_title(), self.title)
        self.assertEqual(self.book.get_authors_firstname(), self.firstname)
        self.assertEqual(self.book.get_authors_surname(), self.surname)
        self.assertEqual(self.book.get_description(), self.description)

    def test_update_methods(self):
        
        self.title = "Lalka"
        self.firstname = "Bolseław"
        self.surname = "Prus"
        self.description = "Historia Stanisława Wokulskiego"

        self.book.update_title(self.title)
        self.book.update_authors_firstname(self.firstname)
        self.book.update_authors_surname(self.surname)
        self.book.update_description(self.description)

        self.assertEqual(self.book.get_title(), self.title)
        self.assertEqual(self.book.get_authors_firstname(), self.firstname)
        self.assertEqual(self.book.get_authors_surname(), self.surname)
        self.assertEqual(self.book.get_description(), self.description)

    def test_repr(self):
        self.assertEqual(repr(self.book), f"{self.book.get_ID()} {self.book.get_authors_firstname()} {self.book.get_authors_surname()} {self.book.get_title()}")

    def test_print(self):
        self.assertEqual(str(self.book), f"\"{self.book.get_title()}\"")
        
    


