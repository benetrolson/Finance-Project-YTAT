# Franco's Budget and Expenses function's
from helper import *
import datetime
from m_functions import *

def view_entries(user):
    print("What kind of entry would you like to view?\n")
    print("1. Income\n2. Expenses\n3. Savings\n4. All Entries")

    choice = inputchecker(4)

    if choice == 1:
        incomes = user.income.keys()
        for income in incomes:
            print(incomes[income])
    elif choice == 2:
        expenses = user.expense.keys()
        for expense in expenses:
            print(expenses[expense])
    elif choice == 3:
        savings = user.saving.keys()
        for saving in savings:
            print(savings[saving])
    elif choice == 4:
        entries = user.income.keys() + user.expense.keys() + user.saving.keys()
        for entry in entries:
            print(entries[entry])
    else:
        print("Invalid choice. Please try again.")

def additem(user):
    print("Is this an:\n1. Income\n2. Saving\n3. Expense")
    choice = inputchecker(3)
    match choice:
        case 1:
            entrytype = "income"
        case 2:
            entrytype = "saving"
        case 3: 
            entrytype = "expense"

    itemname = input("What is the name of this item:\n")
    print("1. USD\n2. IRR\n3. EUR\n4. JPY\n5. GBP\n6. CHF\n7. CAD\n8. AUD\n9. SEK")
    curr = inputchecker(9)

    match curr:
        case 1:
            currency = "USD"
        case 2:
            currency = "IRR"
        case 3:
            currency = "EUR"
        case 4:
            currency = "JPY"
        case 5:
            currency = "GBP"
        case 6:
            currency = "CHF"
        case 7:
            currency = "CAD"
        case 8:
            currency = "AUD"
        case 9:
            currency = "SEK"

    itemscost = input("How much money was this item (in the currency you inputted broski)? (if it's an expense, put a negative number):\n")
    itemscost = gummysint(itemscost)

    category = input("What is the category (ex: transport, entertainment, etc) of this item?:\n")

    if entrytype == "saving":
        saveamount = input("How much do you need to save?\n")
        saveamount = gummysint(saveamount)
    
    todaysday = datetime.datetime.now()

    if entrytype == "income":
        user.incomes[itemname] = Income(itemname, itemscost, currency, category, todaysday)
    elif entrytype == "saving":
        user.savings[itemname] = Saving(itemname, itemscost, currency, category, todaysday)
    elif entrytype == "expense":
        user.expenses[itemname] = Expense(itemname, itemscost, currency, category, todaysday)


def removeitem(user):
    print("Is this an:\n1. Income\n2. Saving\n3. Expense")
    choice = inputchecker(3)
    match choice:
        case 1:
            entrytype = "income"
        case 2:
            entrytype = "saving"
        case 3: 
            entrytype = "expense"

    itemname = input("What is the name of this item:\n")

    if entrytype == "income":
        user.incomes.pop(itemname)
    elif entrytype == "saving":
        user.savings.pop(itemname)
    elif entrytype == "expense":
        user.expenses.pop(itemname)
    else:
        print("That item likely does not exist :(")

def currchange(user):
    print("What currency would you like to change to?\n1. USD\n2. IRR\n3. EUR\n4. JPY\n5. GBP\n6. CHF\n7. CAD\n8. AUD\n9. SEK")
    curr = inputchecker(9)

    match curr:
        case 1:
            currency = "USD"
        case 2:
            currency = "IRR"
        case 3:
            currency = "EUR"
        case 4:
            currency = "JPY"
        case 5:
            currency = "GBP"
        case 6:
            currency = "CHF"
        case 7:
            currency = "CAD"
        case 8:
            currency = "AUD"
        case 9:
            currency = "SEK"

    print("Is the entry an:\n1. Income\n2. Saving\n3. Expense")

    entrytype = inputchecker(3)

    match entrytype:
        case 1:
            entrytype = "income"
        case 2:
            entrytype = "saving"
        case 3: 
            entrytype = "expense"

    while True:
        entry = input("What is the name of the entry you want to change?(Enter 'EXIT' to go back)\n")

        entries = user.income.keys()+user.expense.keys()+user.saving.keys()

        if entry == "EXIT" or entry == "exit":
            return
        elif entry in entries:
            break
        else:
            print("Looks like that entry doesn't exist! Maybe you made a typo? Try again!")
    
    if entrytype == "income":
        user.income[entry].convert(currency)
    elif entrytype == "saving":
        user.saving[entry].convert(currency)
    elif entrytype == "expense":
        user.expense[entry].convert(currency)