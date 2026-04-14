from helper import *
from b_functions import *
from j_functions import *
import sys

def main():
    print("Welcome to the Y. T. A. T. Finance Tracker! ")
    user = csv_to_dictionary()
    while True:
        check = choice_input(["1", "2", "3", "4", "5", "6", "7"], "Would you like to: \n1. View your entries \n2. Add an entry \n3. Delete an entry\n4. View statistics \n5. Change your currency\n6. View Totals \n7. Log out \n> ")
        if check == "1":
            user.view_entries()
        elif check == "2":
            user.additem()
        elif check == "3":
            user.removeitem()
        elif check == "4":
            choice = choice_input(["1", "2"], "Would you like to \n1. View a bar chart \n2. View a pie chart \n> ")
            if choice == "1":
                bargraph(user.categories, user.expenses)
            elif choice == "2":
                piegraph(user.categories, user.expenses)
        elif check == "6":
            entry = user.selectentry()
            entry.currchange()
        else:
            break
        dict_to_csv(user)
     
    sys.exit()
