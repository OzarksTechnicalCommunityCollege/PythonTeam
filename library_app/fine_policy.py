from datetime import datetime

class FinePolicy:
    def __init__(self, daily_rate=0.50, fine_threshold=10.00):
        self.daily_rate = daily_rate
        self.fine_threshold = fine_threshold

    def calculate_fine(self, due_date, return_date):
        if return_date <= due_date:
            return 0.0
        days_late = (return_date - due_date).days
        return days_late * self.daily_rate

    # test_fine_policy.py
from datetime import datetime
from fine_policy import FinePolicy


def test_no_fine_when_returned_on_due_date():
    policy = FinePolicy(daily_rate=1.00)
    due = datetime(2024, 1, 10)
    returned = datetime(2024, 1, 10)

    fine = policy.calculate_fine(due, returned)

    assert fine == 0.0


def test_no_fine_when_returned_before_due_date():
    policy = FinePolicy(daily_rate=1.00)
    due = datetime(2024, 1, 10)
    returned = datetime(2024, 1, 9)

    fine = policy.calculate_fine(due, returned)

    assert fine == 0.0


def test_fine_accrues_after_due_date():
    policy = FinePolicy(daily_rate=0.50)
    due = datetime(2024, 1, 10)
    returned = datetime(2024, 1, 13)  # 3 days late

    fine = policy.calculate_fine(due, returned)

    assert fine == 3 * 0.50


def test_fine_uses_configurable_daily_rate():
    policy = FinePolicy(daily_rate=2.00)
    due = datetime(2024, 1, 10)
    returned = datetime(2024, 1, 12)  # 2 days late

    fine = policy.calculate_fine(due, returned)

    assert fine == 4.00
