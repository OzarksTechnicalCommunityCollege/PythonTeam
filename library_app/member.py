from datetime import datetime

class Member:
    def __init__(self, name):
        self.name = name
        self.checked_out_books = {}  # isbn → due_date
        self.outstanding_fines = 0.0

    def can_check_out(self, fine_policy):
        return self.outstanding_fines < fine_policy.fine_threshold

    def add_book(self, isbn, due_date):
        self.checked_out_books[isbn] = due_date

    def return_book(self, isbn, return_date, fine_policy):
        if isbn not in self.checked_out_books:
            return 0.0

        due_date = self.checked_out_books.pop(isbn)
        fine = fine_policy.calculate_fine(due_date, return_date)
        self.outstanding_fines += fine
        return fine

    def pay_fine(self, amount):
        self.outstanding_fines = max(0.0, self.outstanding_fines - amount)

    def get_balance(self):
        return self.outstanding_fines

    # test_member.py
from datetime import datetime
from member import Member
from fine_policy import FinePolicy


def test_member_adds_book_with_due_date():
    member = Member("Ayden")
    due_date = datetime(2024, 1, 10)

    member.add_book("ABC123", due_date)

    assert "ABC123" in member.checked_out_books
    assert member.checked_out_books["ABC123"] == due_date

    def test_member_return_book_no_fine_if_on_time():
    member = Member("Micah")
    policy = FinePolicy(daily_rate=1.00)

    due = datetime(2024, 1, 10)
    member.add_book("ABC123", due)

    fine = member.return_book("ABC123", datetime(2024, 1, 10), policy)

    assert fine == 0.0
    assert member.outstanding_fines == 0.0
    assert "ABC123" not in member.checked_out_books


def test_member_return_book_with_fine():
    member = Member("Nick")
    policy = FinePolicy(daily_rate=1.00)

    due = datetime(2024, 1, 10)
    member.add_book("ABC123", due)

    fine = member.return_book("ABC123", datetime(2024, 1, 13), policy)

    assert fine == 3.0
    assert member.outstanding_fines == 3.0