# procedural_version/library_procedural.py

def add_book(books, book_id, title, author, total_copies):
    """Add a new book to the library"""
    new_book = {
        "id": book_id,
        "title": title,
        "author": author,
        "total_copies": total_copies,
        "available_copies": total_copies
    }
    books.append(new_book)
    print(f"Book '{title}' added successfully!")


def add_member(members, member_id, name, email):
    """Register a new library member"""
    new_member = {
        "id": member_id,
        "name": name,
        "email": email,
        "borrowed_books": []
    }
    members.append(new_member)
    print(f"Member '{name}' registered successfully!")


def find_book(books, book_id):
    """Find a book by its ID"""
    for book in books:
        if book["id"] == book_id:
            return book
    return None


def find_member(members, member_id):
    """Find a member by their ID"""
    for member in members:
        if member["id"] == member_id:
            return member
    return None


def borrow_book(books, members, borrowed_books, member_id, book_id):
    """Borrow a book from the library"""
    member = find_member(members, member_id)
    book = find_book(books, book_id)

    if not member:
        print("Error: Member not found!")
        return
    if not book:
        print("Error: Book not found!")
        return
    if book["available_copies"] <= 0:
        print("Error: No copies available!")
        return
    if len(member["borrowed_books"]) >= 3:
        print("Error: Borrowing limit reached!")
        return

    book["available_copies"] -= 1
    member["borrowed_books"].append(book_id)
    borrowed_books.append({
        "member_id": member_id,
        "book_id": book_id,
        "member_name": member["name"],
        "book_title": book["title"]
    })
    print(f"{member['name']} borrowed '{book['title']}' successfully!")


def return_book(books, members, borrowed_books, member_id, book_id):
    """Return a borrowed book to the library"""
    member = find_member(members, member_id)
    book = find_book(books, book_id)

    if not member:
        print("Error: Member not found!")
        return
    if not book:
        print("Error: Book not found!")
        return
    if book_id not in member["borrowed_books"]:
        print("Error: This member hasn't borrowed this book!")
        return

    book["available_copies"] += 1
    member["borrowed_books"].remove(book_id)

    for transaction in borrowed_books:
        if transaction["member_id"] == member_id and transaction["book_id"] == book_id:
            borrowed_books.remove(transaction)
            break

    print(f"{member['name']} returned '{book['title']}' successfully!")


def display_available_books(books):
    """Display all available books"""
    print("\n=== Available Books ===")
    for book in books:
        if book["available_copies"] > 0:
            print(
                f"{book['title']} by {book['author']} ({book['available_copies']} copies available)")


def display_member_books(members, books, member_id):
    """Display books borrowed by a member"""
    member = find_member(members, member_id)
    if not member:
        print("Error: Member not found!")
        return

    print(f"\n=== Books borrowed by {member['name']} ===")
    if not member["borrowed_books"]:
        print("No books currently borrowed")
        return

    for book_id in member["borrowed_books"]:
        book = find_book(books, book_id)
        if book:
            print(f"- {book['title']} by {book['author']}")
