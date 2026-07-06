CLI_expenses;

this short python project allows the user to manage expenses through terminal;

**features**: 
- Add new expenses with category, amount, and description
- View all expenses or filter by category
- View statistics: total spending and breakdown by category
- Delete expenses by id

**stack**:
- Python 3
- CLI interface(argparse)
- csv

**how to install**:
- clone repository
- navigate to the project folder
- run it(python main.py --help)

**how to use**:

(delete "[]" and write your own data)
- add an expense:
python main.py add --amount [your amount] --category [your category] --description "[your description]"
- list expenses:
python main.py list --category [your category] // everything after list is optional, you might use filter to display data by each category
- view stats:
python main.py stats
- delete an expense by id:
python main.py delete --id [id you want to delete]

**structure**:
- main.py     // main script
- models.py   // data class
- storage.py  // csv reader/writer
- expenses.csv // file with data

