# library_management.py

class Book:
    """A simple Book class to hold book data and its availability state."""

    def __init__(self, title, author):
        # Public attributes anyone can read: title and author
        self.title = title
        self.author = author
        # Private-ish attribute (by convention): indicates if the book is checked out
        # Leading underscore signals: "internal use, don't touch directly"
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out (unavailable)."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True  # indicates success
        return False     # already checked out

    def return_book(self):
        """Mark the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True   # indicates success
        return False      # was not checked out

    def is_available(self):
        """Utility method to check availability."""
        return not self._is_checked_out

    def __str__(self):
        """String representation used when printing the Book."""
        return f"{self.title} by {self.author}"


class Library:
    """A Library class that manages a collection of Book objects."""

    def __init__(self):
        # Private list of books; library manages Book instances here
        self._books = []

    def add_book(self, book):
        """Add a Book instance to the library collection."""
        # We expect 'book' to be an instance of Book
        self._books.append(book)

    def _find_book_by_title(self, title):
        """
        Internal helper to find the first book with a matching title.
        Returns the Book instance or None if not found.
        """
        for book in self._books:
            if book.title == title:
                return book
        return None

    def check_out_book(self, title):
        """
        Attempt to check out a book by title.
        If found and available, mark it checked out and return True.
        Otherwise return False.
        """
        book = self._find_book_by_title(title)
        if book is None:
            # Book not in our collection
            return False
        return book.check_out()  # Book.check_out handles availability

    def return_book(self, title):
        """
        Attempt to return a book by title.
        If found and currently checked out, mark it available and return True.
        Otherwise return False.
        """
        book = self._find_book_by_title(title)
        if book is None:
            return False
        return book.return_book()

    def list_available_books(self):
        """Print all books that are currently available (not checked out)."""
        for book in self._books:
            if book.is_available():
                print(book)
