# Library Management System using OOP

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False

    def show_details(self):
        status = "Issued" if self.is_issued else "Available"
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {status}")


class Library:
    def __init__(self):
        self.books = []

    # Add book
    def add_book(self, book_id, title, author):
        book = Book(book_id, title, author)
        self.books.append(book)
        print("Book added successfully")

    # Show all books
    def show_books(self):
        if not self.books:
            print("No books available")
            return

        for book in self.books:
            book.show_details()

    # Issue book
    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_issued:
                    book.is_issued = True
                    print(f"Book '{book.title}' issued successfully")
                else:
                    print("Book already issued")
                return
        print("Book not found")

    # Return book
    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.is_issued:
                    book.is_issued = False
                    print(f"Book '{book.title}' returned successfully")
                else:
                    print("Book was not issued")
                return
        print("Book not found")


# ---------------- Test Code ----------------

lib = Library()

lib.add_book(101, "Python Basics", "John Doe")
lib.add_book(102, "Data Structures", "Robert")

print("\nAll Books:")
lib.show_books()

print("\nIssue Book:")
lib.issue_book(101)

print("\nAfter Issue:")
lib.show_books()

print("\nReturn Book:")
lib.return_book(101)

print("\nAfter Return:")
lib.show_books()