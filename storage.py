import csv
import os
from models import Expense


def save(expenses, filename="expenses.csv"):
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["id", "date", "category", "amount", "description"])
        for expense in expenses:
            writer.writerow([expense.id, expense.date, expense.category, expense.amount, expense.description])

def load(filename="expenses.csv"):
    expenses = []
    if not os.path.exists(filename):
        return expenses
    with open(filename, "r", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            expenses.append(Expense(int(row["id"]), row["date"], row["category"], float(row["amount"]), row["description"]))
        return expenses