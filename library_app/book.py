"""
Represents a single book title in the library catalog.
One Book instance represents all copies of that title.
"""
from datetime import datetime, timedelta

class Book:
    """Defines book class constructor"""
    def __init__(self, title: str, author: str, isbn: str, total_copies: int):
        if not title or not title.strip():
            raise ValueError("Title cannot be empty.")
        if not author or not author.strip():
            raise ValueError("Author cannot be empty.")
        if not isbn or not isbn.strip():
            raise ValueError("ISBN cannot be empty.")
        if total_copies < 0:
            raise ValueError("Total copies cannot be negative.")

        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = total_copies
        self.available_copies = total_copies
        self.checkout_date = None
        self.due_date = None
        self.member_check_out = None

    @property
    def is_available(self) -> bool:
        """Returns a true or false value if available copies falls below 0"""
        return self.available_copies > 0

    def is_overdue(self) -> bool:
        """Returns True if book is past its due date"""
        if self.due_date is None:
            return False
        return datetime.now() > self.due_date

    def check_out(self) -> None:
        """Reduces available copies by one"""
        if not self.is_available:
            raise RuntimeError(f"No available copies of '{self.title}' to check out.")

        self.available_copies -= 1
        self.checkout_date = datetime.now()
        self.due_date = self.checkout_date + timedelta(days=14)

    def return_book(self) -> None:
        """Adds one to available copies for requested book"""
        if self.available_copies >= self.total_copies:
            raise RuntimeError(f"All copies of '{self.title}' are already returned.")
        self.available_copies += 1
