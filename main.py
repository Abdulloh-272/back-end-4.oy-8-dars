class Book:
    def __init__(self, name, author, genre, copies=1):
        self.name = name           
        self.author = author       
        self.genre = genre         
        self.copies = copies       

    def get_copy(self):
        self.copies += 1
        print(f"{self.name} nusxasi olindi. Hozirda {self.copies} nusxasi mavjud.")
    
    def return_copy(self):
        if self.copies > 0:
            self.copies -= 1
            print(f"{self.name} nusxasi qaytarildi. Hozirda {self.copies} nusxasi mavjud.")
        else:
            print(f"{self.name} kitobining nusxalari yo'q, qaytarish mumkin emas.")

    def get_info(self):
        return f"Kitob nomi: {self.name}, Muallifi: {self.author}, Janri: {self.genre}, Nusxalar soni: {self.copies}"

class Library:
    def __init__(self):
        self.books = []  

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(book.get_info())

book1 = Book("Python Programming", "John Doe", "IT", 3)
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Novel")
book3 = Book("1984", "George Orwell", "Dystopia", 2)

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print("Kutubxonadagi kitoblar:")
library.show_books()

print("\nKitob olish va qaytarish:")
book1.get_copy()  
book1.return_copy()   
book2.return_copy() 

print("\nKutubxona kitoblari yangilangan nusxalar bilan:")
library.show_books()
