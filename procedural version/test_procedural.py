# procedural_version/test_procedural.py

from library_procedural import *


def test_library_procedural():
    books = []
    members = []
    borrowed_books = []

    print("="*60)
    print("PROCEDURAL LIBRARY MANAGEMENT SYSTEM - TEST")
    print("="*60)

    add_book(books, 1, "Python Crash Course", "Eric Matthes", 3)
    add_book(books, 2, "Clean Code", "Robert Martin", 2)
    add_book(books, 3, "The Pragmatic Programmer", "Hunt & Thomas", 1)

    add_member(members, 101, "Alice Smith", "alice@email.com")
    add_member(members, 102, "Bob Jones", "bob@email.com")

    display_available_books(books)

    borrow_book(books, members, borrowed_books, 101, 1)
    borrow_book(books, members, borrowed_books, 101, 2)
    borrow_book(books, members, borrowed_books, 102, 3)

    display_member_books(members, books, 101)
    display_available_books(books)

    return_book(books, members, borrowed_books, 101, 1)
    display_available_books(books)

    borrow_book(books, members, borrowed_books, 102, 999)  # Invalid book ID
    return_book(books, members, borrowed_books, 999, 1)    # Invalid member ID


if __name__ == "__main__":
    test_library_procedural()
