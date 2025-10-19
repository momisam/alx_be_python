# library_class.py
# Defines Library and Bank classes

from book_class import Book, PrintBook, EBook

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("Only Book objects can be added to the library.")

    def display_books(self):
        """Print all books in the library"""
        for book in self.books:
            print(book)

    def __str__(self):
        return f"Library with {len(self.books)} books"


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def __str__(self):
        return f"Bank: {self.name} with {len(self.accounts)} accounts"

    def __repr__(self):
        return f"Bank(name='{self.name}', accounts={len(self.accounts)})"
