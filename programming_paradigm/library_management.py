# library_management.py

class Library:
    def __init__(self):
        self._books = []  # Private list to store instances of Book

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return False  # Book not found

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return False  # Book not found

    def list_available_books(self):
        available_books = [book for book in self._books if not book._is_checked_out]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No available books")