class User:
    def __init__(self, name):
        self.name = name
        self.checked_out = {}  # isbn -> due_date
        self.fines = 0.0

    def add_book(self, isbn, due_date):
        self.checked_out[isbn] = due_date

    def remove_book(self, isbn):
        return self.checked_out.pop(isbn, None)

    def add_fine(self, amount):
        self.fines += amount

    def clear_fines(self):
        self.fines = 0.0


