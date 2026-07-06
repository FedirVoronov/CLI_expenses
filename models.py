class Expense:
    def __init__(self, id, date, category, amount, description):
        self.id = id
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def __repr__(self):
        return(f"id = {self.id}; date = {self.date}; category = {self.category}; amount = {self.amount}; description = {self.description};")