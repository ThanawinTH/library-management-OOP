# oop_solution/library_oop.py

class Book:
    """Represents a book in the library"""

    def __init__(self, book_id, title, author, total_copies):
        self.id = book_id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    def borrow(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        return False

    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        return False

    def __str__(self):
        return f"{self.title} by {self.author} ({self.available_copies}/{self.total_copies} available)"


class Member:
    """Represents a library member"""

    def __init__(self, member_id, name, email):
        self.id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []

    def borrow_book(self, book_id):
        if len(self.borrowed_books) < 3:
            self.borrowed_books.append(book_id)
            return True
        return False

    def return_book(self, book_id):
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)
            return True
        return False


class Library:
    """Manages books and members"""

    def __init__(self):
        self.books = []
        self.members = []
        self.borrowed_books = []

    # --- Add Methods ---
    def add_book(self, book_id, title, author, total_copies):
        self.books.append(Book(book_id, title, author, total_copies))
        print(f"Book '{title}' added successfully!")

    def add_member(self, member_id, name, email):
        self.members.append(Member(member_id, name, email))
        print(f"Member '{name}' registered successfully!")

    # --- Find Methods ---
    def find_book(self, book_id):
        return next((book for book in self.books if book.id == book_id), None)

    def find_member(self, member_id):
        return next((member for member in self.members if member.id == member_id), None)

    # --- Borrow and Return ---
    def borrow_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if not member:
            print("Error: Member not found!")
            return False
        if not book:
            print("Error: Book not found!")
            return False
        if not book.borrow():
            print("Error: No copies available!")
            return False
        if not member.borrow_book(book_id):
            print("Error: Member has reached borrowing limit!")
            book.return_book()
            return False

        self.borrowed_books.append({
            'member_id': member_id,
            'book_id': book_id,
            'member_name': member.name,
            'book_title': book.title
        })
        print(f"{member.name} borrowed '{book.title}'")
        return True

    def return_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if not member or not book:
            print("Error: Member or book not found!")
            return False
        if not member.return_book(book_id):
            print("Error: This member hasn't borrowed this book!")
            return False

        book.return_book()
        for i, transaction in enumerate(self.borrowed_books):
            if transaction['member_id'] == member_id and transaction['book_id'] == book_id:
                self.borrowed_books.pop(i)
                break
        print(f"{member.name} returned '{book.title}'")
        return True

    # --- Display Methods ---
    def display_available_books(self):
        print("\n=== Available Books ===")
        for book in self.books:
            if book.available_copies > 0:
                print(book)

    def display_member_books(self, member_id):
        member = self.find_member(member_id)
        if not member:
            print("Error: Member not found!")
            return
        print(f"\n=== Books borrowed by {member.name} ===")
        if not member.borrowed_books:
            print("No books currently borrowed")
        else:
            for book_id in member.borrowed_books:
                book = self.find_book(book_id)
                print(f"- {book.title} by {book.author}")
