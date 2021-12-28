import csv, json
from book import Book

class Library:

    """ Klasa odpowiadajaca za cala funkcjonalnosc bazy danych """

    def __init__(self):

        """ Konstruktor """
        
        self.database = []

    def addBook(self, book):

        """ Funkcja sluzaca do dodawania ksiazek do bazy danych """
        
        if self.size() != 0:
            _id = self.database[-1].get_ID()
        if self.size() == 0:
            _id = 0
        book.update_ID(_id+1)


        is_not_in_database = True
        title = book.get_title()
        for _book in self.database:
            if title.lower() == _book.get_title().lower():
                is_not_in_database = False
        if is_not_in_database:
            if title != "":
                self.database.append(book)
            return 1
        return -1
        
    def removeBook(self, book):

        """ Funkcja sluzaca do usuwania ksiazek z bazy danych """

        if book is not None:
            _id = book.get_ID()
            if book in self.database:
                self.database.remove(book)
            for i in range(_id-1, self.size()):
                new_id = self.database[i].get_ID()-1
                self.database[i].update_ID(new_id)


    def update_book_info(self, book, *args):

        """ Funkcja pozwalajaca modyfikowac poszczegolne atrybuty ksiazki """
        
        if args[1] == "":
            return -1
        if 'title' in args:
            book.update_title(args[1])
        elif 'authors_firstname' in args:
            book.update_authors_firstname(args[1])
        elif 'authors_surname' in args:
            book.update_authors_surname(args[1])
        elif 'description' in args:
            book.update_description(args[1])
        else:
            print("Niepoprawna opcja!")  


    def printAllBooks(self):
        for i in self.database:
            print(repr(i))
    
    def getAllBooks(self):
        return self.database
    
    def import_books_form_csv_file(self, file_name):

        """ Funkcja importujaca baze danych ksiazek z pliku .csv """
        
        try:
            file = open(file_name, "r", encoding="utf-8")
        except FileNotFoundError:
            raise FileNotFoundError
        csv_reader = csv.reader(file)

        counter = 0
        for row in csv_reader:
            if len(row) > 4:
                counter += 1
                splited = row[0].split(";")
                splited[4] = [splited[4]]
                for i in range(1, len(row)):
                    splited[4].append(row[i])
                if splited[0] != 'ID':
                    if splited[1] != "" or splited[2] != "":
                        self.addBook(Book(splited[1], splited[2], splited[3], splited[4]))

        return counter

    
    def import_books_from_json_file(self, file_name):
        
        """ Funkcja importujaca baze danych ksiazek z pliku .json """

        try:
            file = open(file_name, "r", encoding="utf-8")
        except FileNotFoundError:
            raise FileNotFoundError

        books = json.loads(file.read())
        counter = 0
        for book in books:
            self.addBook(Book(
                book['title'], book['authors_firstname'],
                book['authors_surname'], book['description']
                )
            )
            counter += 1

        return counter

    def export_books_to_csv_file(self, file_name):
        
        """ Funkcja eksportujaca baze danych do pliku z rozszerzeniem .csv """
        
        file = open(file_name+".csv", "w", encoding="utf-8", newline="")
        csv_writer = csv.writer(file, delimiter=";")
        counter = 0
        header = "ID;title;authors_firstname;authors_surname;description"
        csv_writer.writerow([header])
        for book in self.database:
            csv_writer.writerow([book.get_ID(), book.get_title(),
                             book.get_authors_firstname(), book.get_authors_surname(),
                             book.get_description()])
            counter += 1

        file.close()
        return counter

    def export_books_to_json_file(self, file_name):
        
        """ Funkcja eksportujaca baze danych do pliku z rozszerzeniem .json """

        file = open(file_name+".json", "w", encoding="utf-8")
        counter = 0
        file.write("[\n")
        for i in range(len(self.database)):
            json.dump(self.database[i].__dict__, file, ensure_ascii=False, indent=4)
            if i != len(self.database)-1:
                file.write(",")
            counter += 1
        file.write("\n]")
        file.close()
        return counter

    def export_books_to_txt_file(self, file_name):
        """ Funkcja eksportujaca baze danych do pliku z rozszerzeniem .txt """

        file = open(file_name+".txt", "w", encoding="utf-8")
        counter = 0
        header = "ID,title,authors_firstname,authors_surname,description"
        file.write(header)
        for book in self.database:
            file.write(f"\n{book.get_ID()},{book.get_title()},{book.get_authors_firstname()}, {book.get_authors_surname()}, {book.get_description()}")
            counter += 1

        file.close()
        return counter
        

    def find_book_by_title(self, title):
        """ Funkcja wyszukujaca ksiazke w bazie danych za pomoca tytulu"""
        for book in self.database:
            if book.get_title().lower() == title.lower():
                return book
            
        return None

    def find_book_by_ID(self, ID):
        """ Funkcja wyszukujaca ksiazke w bazie danych za pomoca ID """
        for book in self.database:
            if book.get_ID() == int(ID):
                return book
        
        return None

    def size(self):
        return len(self.database)

    