import argparse
import datetime

from storage import save, load
from models import Expense

parser = argparse.ArgumentParser(description = "this CLI looks for an expense and saves it")

subparsers = parser.add_subparsers(dest = "command")

add_parser = subparsers.add_parser("add", help = "add an expense")
add_parser.add_argument("--amount", type = float, required = True,  help = "amount spent")
add_parser.add_argument("--category", type = str, required = True, help = "category of the expense")
add_parser.add_argument("--description", type = str, default = "", help = "description of the expense")

list_parser = subparsers.add_parser("list", help = "list all expenses")
list_parser.add_argument("--category", type = str, default = None, help = "category of the expense")

delete_parser = subparsers.add_parser("delete", help="delete item by id")
delete_parser.add_argument("--id", type=int, required=True, help="id of item to delete")

stats_parser = subparsers.add_parser("stats", help = "show expenses stats")

args = parser.parse_args()

if args.command == "add":
    expenses = load()
    id = len(expenses) + 1
    date = str(datetime.date.today())
    new_expense = Expense(id, date, args.category, args.amount, args.description)
    expenses.append(new_expense)
    save(expenses)
    print(f"expense added (id={id})")
elif args.command == "list":
    expenses = load()
    if args.category is not None:
        filtered = []
        for expense in expenses:
            if expense.category == args.category:
                filtered.append(expense)
        expenses = filtered
        for expense in expenses:
            print(expense)
elif args.command == "stats":
    expenses = load()
    Sum = 0
    sort_category = {}
    for expense in expenses:
        if expense.category in sort_category:
            sort_category[expense.category] += expense.amount
        else:
            sort_category[expense.category] = expense.amount
        Sum += expense.amount
    print(f"Expenses total: {Sum}")
    for category, amount in sort_category.items():
        print(f"{category}: {amount}")
elif args.command == "delete":
    expenses = load()
    new_expense = []
    for expense in expenses:
        if expense.id != args.id:
            new_expense.append(expense)
    save(new_expense)
    print(f"expense deleted (id={args.id})")

