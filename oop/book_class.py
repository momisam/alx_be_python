class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        # Matches expected format
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        # Matches expected format
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        # Matches expected format
        print(f"Deleting {self.title}")
