# A Basic Library Management System utilizing OOP and Exception Handling.
# Functionalities: add books, borrow books, return books, check book's availability.

class Book:

    def __init__(self, title, author, units):
        self.title = title
        self.author = author
        self.units = units


    def check_availability(self):
        if self.units > 0:
            print(f"{self.units} units of '{self.title}' are available.")
        else:
            print(f"Sorry!, '{self.title}' is currently unavailable.")



class Library:
    
    books = []
    
    def add_book(self, book):
        self.books.append(book)


    def borrow_book(self, book):
        for lib_book in self.books:
            if lib_book.title == book.title:
                if lib_book.units > 0:
                    lib_book.units -= 1
                    
                    return True
                else:
                    return False
                    
                
        return False
    

    def return_book(self, book):
        for lib_book in self.books:
            if lib_book.title == book.title:
                lib_book.units += 1
                print("Book returned successfuly!")
                return
        raise Exception(f"{book.title} not found in the library.")
    

class Member:
            
    def __init__(self, member_id, name, max_books=5, library=None):
        self.member_id = member_id
        self.name = name
        self.max_books = max_books
        self.borrowed_books = []
        self.library = library


    def borrow_book(self, book):
        if len(self.borrowed_books) < self.max_books:
            if self.library.borrow_book(book):   
                self.borrowed_books.append(book)
                print(f"'{book.title}' has been successfully borrowed by {self.name}")
                return
            else:
                raise Exception(f"Sorry! '{book.title}' is unavailable or not found.")
        else:
            raise Exception(f"{self.name} has reached the maximum borrow limit.")


    def return_book(self, book):
        if book not in self.borrowed_books:
            raise Exception(f"{self.name} has not borrowed '{book.title}'")
        
        self.library.return_book(book)
        self.borrowed_books.remove(book)
        print(f"'{book.title}' has been returned by {self.name}.")
        return
    

book1 = Book("Harry Potter", "J.K. Rowling", 1)
book2 = Book("The Hobbit", "J.R.R. Tolkien", 5)
book3 = Book("Jnana Yoga", "Swami Vivekananda", 2)
# book4 = Book("Words of the master", "Ramakrishna Paramahamsa", 1)
# book5 = Book("Raja Yoga", "Swami Vivekananda", 2)
# book6 = Book("Advaita Vedanta: General Science of Living", "Swami Vivekananda", 2)

library = Library()

library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)
# library.add_book(book4)
# library.add_book(book5)
# library.add_book(book6)

m1 = Member(1, "Anuvansh", library=library)
# m1.borrow_book(book3)
# m1.borrow_book(book4)
# m1.borrow_book(book2)
m1.borrow_book(book1)
# m1.borrow_book(book5)

# m1.return_book(book1)
# m1.return_book(book2)
# m1.return_book(book6)
book1.check_availability()





    