class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        # User-friendly display
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        # Developer/debug display
        return f"Book(title='{self.title}', author='{self.author}')"

    def __del__(self):
        # Called automatically when the object is deleted
        print(f"Deleting book: {self.title} by {self.author}")
