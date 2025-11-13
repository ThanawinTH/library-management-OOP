# Library Management System (OOP Version)

This project refactors a procedural-style Library Management System into an object-oriented design using Python.  
It demonstrates encapsulation, modularity, and data abstraction using `Book`, `Member`, and `Library` classes.

## Design Overview

### `Book`

- **Attributes:** id, title, author, total_copies, available_copies
- **Methods:** `borrow()`, `return_book()`, `__str__()`

### `Member`

- **Attributes:** id, name, email, borrowed_books
- **Methods:** `borrow_book()`, `return_book()`

### `Library`

- **Attributes:** collections of books, members, borrowed_books
- **Methods:** `add_book()`, `add_member()`, `find_book()`, `find_member()`,  
  `borrow_book()`, `return_book()`, `display_available_books()`, `display_member_books()`

## Testing

### Test Coverage

- Adding books and members
- Borrowing and returning books
- Displaying available books and borrowed books
- Handling edge cases (unavailable books, invalid IDs, borrow limit exceeded)

### Run Test

```bash
python oop_solution/test_oop.py
```
