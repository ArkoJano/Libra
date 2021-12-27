import csv, json
from typing import Counter
from book import Book

class Library:

    def __init__(self):
        self.database = []

    def addBook(self, book):
        if self.size() != 0:
            _id = self.database[-1].get_ID()
            book.update_ID(_id+1)
        self.database.append(book)
        
    def removeBook(self, book):
        if book is not None:
            _id = book.get_ID()
            if book in self.database:
                self.database.remove(book)
            for i in range(_id-2, self.size()):
                new_id = self.database[i].get_ID()-1
                self.database[i].update_ID(new_id)


    def update_book_info(self, book, *args):
        
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
        try:
            file = open(file_name, "r", encoding="utf-8")
        except FileNotFoundError:
            raise FileNotFoundError
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(len(row))
            if len(row) > 4:
                splited = row[0].split(";")
                splited[4] = [splited[4]]
                for i in range(1, len(row)):
                    splited[4].append(row[i])
                
                if splited[0] != 'ID':
                    if splited[1] != "" or splited[2] != "":
                        self.database.append(Book(splited[1], splited[2], splited[3], splited[4]))
            

    def export_books_to_csv_file(self, file_name):
        file = open(file_name+".csv", "w", encoding="utf-8")
        csv_writer = csv.writer(file, delimiter=";")
        counter = 0
        header = "ID,title,authors_firstname,authors_surname"
        csv_writer.writerow([header])
        for book in self.database:
            csv_writer.writerow([book.get_ID(), book.get_title(),
                             book.get_authors_firstname(), book.get_authors_surname()])
            counter += 1

        file.close()
        return counter

    def export_books_to_json_file(self, file_name):
        file = open(file_name+".json", "w", encoding="utf-8")
        counter = 0
        for book in self.database:
            json.dump(book.to_dict(), file, ensure_ascii=False, indent=4)
            print(book.to_dict())
            counter += 1

        file.close()
        return counter
        

    def find_book_by_title(self, title):
        for book in self.database:
            if book.get_title().lower() == title.lower():
                return book
            
        return None

    def find_book_by_ID(self, ID):
        for book in self.database:
            if book.get_ID() == int(ID):
                return book
        
        return None

    def size(self):
        return len(self.database)

    