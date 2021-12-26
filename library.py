import csv
from book import Book

class Library:

    def __init__(self):
        self.database = []

    def addBook(self, book):
        _id = self.database[-1].get_ID()
        book.update_ID(_id + 1)
        self.database.append(book)
        # print("Dodano: ", book, " do bazy danych.")

    def removeBook(self, book):
        _id = book.get_ID()
        if book in self.database:
            self.database.remove(book)
        for i in range(_id-1, self.size()):
            self.database[i].update_ID(self.database[i].get_ID()-1)

    def update_book_info(self, title, *args):
        book = self.find_book_by_title(title)
        menu = """" Którą kolumnę chcesz zaktualizować?
                1. Tytuł
                2. Imię autora
                3. Nazwisko autora
        """
        print(menu, end="")
        option = input("Do zmiany: ")
        if option == 1:
            new_title = input("Podaj nowy tytuł: ")
            book.update_title(new_title)
        elif option == 2:
            new_authors_firstname = input("Podaj nowe imię: ")
            book.update_title(new_authors_firstname)
        elif option == 3:
            new_authors_surname = input("Podaj nowe nazwisko: ")
            book.update_title(new_authors_surname)
        else:
            print("Niepoprawna opcja!")  


    def printAllBooks(self):
        for i in self.database:
            print(repr(i))
    
    def getAllBooks(self):
        return self.database
    
    def import_books_form_csv_file(self, file):
        csv_reader = csv.reader(file)
        for row in csv_reader:
            splited = row[0].split(";")
            if splited[0] != 'ID':
                if splited[1] != "" or splited[2] != "":
                    self.database.append(Book(splited[1], splited[2], splited[3]))
            

    def export_books_to_csv_file(self, file_name):
        file = open(file_name, "w", encoding="utf-8")
        csv_writer = csv.writer(file, delimiter=";")

        header = "ID,title,authors_firstname,authors_surname"
        csv_writer.writerow([header])
        for book in self.database:
            csv_writer.writerow([book.get_ID(), book.get_title(),
                             book.get_authors_firstname(), book.get_authors_surname()])
        
        file.close()

    def find_book_by_title(self, title):
        for book in self.database:
            if book.get_title() == title:
                return book
            
        return None

    def find_book_by_ID(self, ID):
        for book in self.database:
            if book.get_ID() == int(ID):
                return book
        
        return None

    def size(self):
        return len(self.database)

    