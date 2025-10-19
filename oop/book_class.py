# book_class.py
# Defines Book, PrintBook, and EBook classes

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """User-friendly string representation"""
        return f"'{self.title}' by {self.author} ({self.year})"

    def __repr__(self):
        """Developer-friendly representation"""
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"


class PrintBook(Book):
    def __init__(self, title, author, year, pages):
        super().__init__(title, author, year)
        self.pages = pages

    def __str__(self):
        """String representation for print books"""
        return f"'{self.title}' by {self.author} ({self.year}) - {self.pages} pages"

    def __repr__(self):
        return f"PrintBook(title='{self.title}', author='{self.author}', year={self.year}, pages={self.pages})"


class EBook(Book):
    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size = file_size

    def __str__(self):
        """String representation for ebooks"""
        return f"'{self.title}' by {self.author} ({self.year}) - {self.file_size}MB"

    def __repr__(self):
        return f"EBook(title='{self.title}', author='{self.author}', year={self.year}, file_size={self.file_size})"
