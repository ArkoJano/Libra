
class Book:

    _id = 1
    
    def __init__(self, title, 
                authors_firstname, authors_surname):
        self.ID = Book._id
        self.title = title
        self.authors_firstname = authors_firstname
        self.authors_surname = authors_surname
        Book._id += 1

    def __str__(self) -> str:
        return f"\"{self.title}\""

    def __repr__(self):
        return f"{self.ID} {self.authors_firstname} {self.authors_surname} {self.title}"

    def get_ID(self):
        return self.ID
    
    def get_title(self):
        return self.title
    
    # def get_side_title(self):
    #     return self.side_title

    def get_authors_firstname(self):
        return self.authors_firstname

    def get_authors_surname(self):
        return self.authors_surname

    def get_author(self):
        return str(self.authors_firstname + " " + self.authors_surname)

    # def get_publisher(self):
    #     return self.publisher
    
    # def get_date_of_publish(self):
    #     return self.date_of_publish

    def update_ID(self, new_ID):
        self.ID = new_ID

    def update_title(self, new_title):
        self.title = new_title

    # def update_side_title(self, new_side_title):
    #     self.side_title = new_side_title

    def update_authors_firstname(self, new_firstname):
        self.authors_firstname = new_firstname

    def update_authors_surname(self, new_surname):
        self.authors_surname = new_surname

    # def update_date_of_publish(self, new_date):
    #     self.date_of_publish = new_date
    
    # def update_publisher(self, new_publisher):
    #     self.publisher = new_publisher

    
