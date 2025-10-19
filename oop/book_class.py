class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        # User-friendly string representation
        return f"'{self.title}' by {self.author} ({self.year})"

    def __repr__(self):
        # Developer-friendly representation
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"

    def __del__(self):
        # Called automatically when an object is deleted
        print(f"Deleting book: {self.title} by {self.author} ({self.year})")
