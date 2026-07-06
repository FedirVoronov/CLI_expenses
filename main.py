import argparse
from operator import add

from storage import save, load
from models import Expense

parser = argparse.ArgumentParser(description = "this CLI looks for an expense and saves it")

subparsers = parser.add_subparsers(dest = "command")

add_parser = subparsers.add_parser("add", help = "add an expense")
add_parser.add_argument("--amount", type = float, required = True,  help = "amount spent")
add_parser.add_argument("--category", type = str, required = True, help = "category of the expense")
add_parser.add_argument("--description", type = str, default = "", help = "description of the expense")


