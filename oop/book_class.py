# book_class.py

class Book:
    """
    A simple Book class demonstrating Python magic methods:
    - __init__ : constructor
    - __del__  : destructor (prints a deletion message)
    - __str__  : human-friendly string representation
    - __repr__ : official string representation suitable for debugging/recreation
    """

    def __init__(self, title: str, author: str, year: int):
        """
        Initialize a new Book instance.

        Parameters:
            title (str): Title of the book.
            author (str): Author of the book.
            year (int): Publication year.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor called when the object is about to be destroyed.
        Prints a message indicating which book is being deleted.
        """
        # Use getattr to defensively access title in case attributes are cleared during interpreter shutdown.
        title = getattr(self, "title", "<unknown>")
        print(f"Deleting {title}")

    def __str__(self) -> str:
        """
        Human-friendly string representation used by print() and str().
        Example: "1984 by George Orwell, published in 1949"
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        """
        Official string representation used by repr() and the interactive interpreter.
        Should ideally be a valid Python expression that recreates the object.
        Example: "Book('1984', 'George Orwell', 1949)"
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
