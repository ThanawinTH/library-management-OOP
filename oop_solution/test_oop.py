# oop_solution/test_oop.py
from library_oop import Library


def test_library_oop():
    lib = Library()

    print("="*60)
    print("OOP LIBRARY MANAGEMENT SYSTEM - TEST")
    print("="*60)

    lib.add_book(1, "Python Crash Course", "Eric Matthes", 3)
    lib.add_book(2, "Clean Code", "Robert Martin", 2)
    lib.add_book(3, "The Pragmatic Programmer", "Hunt & Thomas", 1)
    lib.add_member(101, "Alice Smith", "alice@email.com")
    lib.add_member(102, "Bob Jones", "bob@email.com")

    lib.display_available_books()

    lib.borrow_book(101, 1)
    lib.borrow_book(101, 2)
    lib.borrow_book(102, 3)
    lib.display_member_books(101)
    lib.display_available_books()

    lib.return_book(101, 1)
    lib.display_available_books()

    lib.borrow_book(102, 999)  # invalid book
    lib.return_book(999, 1)    # invalid member


if __name__ == "__main__":
    test_library_oop()
