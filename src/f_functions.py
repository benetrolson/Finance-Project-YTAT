# Franco's Budget and Expenses function's
from helper import *

def view_entries(user):
    print("What kind of entry would you like to view?\n")
    print("1. Income\n2. Expenses\n3. Savings\n4. All Entries")

    choice = inputchecker(4)

    for entry in user.entries:
        if choice == 1 and entry.type == "income":
            print(entry.name)
            print(f"  {entry.amount}\n  {entry.date}\n  {entry.category}")
        elif choice == 2 and entry.type == "expense":
            print(entry.name)
            print(f"  {entry.amount}\n  {entry.date}\n  {entry.category}")
        elif choice == 3 and entry.type == "saving":
            print(entry.name)
            print(f"  {entry.amount}\n  {entry.date}\n  {entry.goal_date}\n  {entry.category}")
        elif choice == 4:
            print(f"{entry.name} : {entry.type}")
            print(f"  {entry.amount}\n  {entry.date}\n  {entry.category}")
        else:
            pass
