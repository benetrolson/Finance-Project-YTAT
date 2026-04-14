#MW_CP2 classes
import pandas as pd
from helper import *
import datetime

##Class Budget: (aggregate with currency, income, expenses, savings)
class Budget:
#init there will 
    ###explanation: this class is an aggregate class, that holds all possible currencies the player can use, as well as all of their budgeting choices. (this includes income, savings, and expenses)
	#1: income
	#2: expenses
	#3: Savings
	#4: current currency
    def __init__(self, income, expenses, savings, budgets, current_currencies):
        self.incomes = income
        self.expenses = expenses
        self.savings = savings
        self.current_currencies = current_currencies
        self.budgets = budgets
        self.categories = []
        for i in self.incomes:
            self.categories.append(self.incomes[i].category)
        for i in self.expenses:
            self.categories.append(self.expenses[i].category)
        for i in self.savings:
            self.categories.append(self.savings[i].category)
        for i in self.budgets:
            self.categories.append(self.budgets[i].category)
    def selectentry(self):
        # Used to get a specific entry as an object
        print("Is this an:\n1. Income\n2. Saving\n3. Expense\n4. Budget\n")
        choice = inputchecker(4)
        match choice:
            case 1:
                entrytype = "income"
            case 2:
                entrytype = "saving"
            case 3: 
                entrytype = "expense"
            case 4:
                entrytype = "budget"
            
        name = input("What is the name of the entry?\n")

        if entrytype == "expense":
            if name in self.expenses.keys():
                return self.expenses[name]
        elif entrytype == "income":
            if name in self.incomes.keys():
                return self.incomes[name]
        elif entrytype == "saving":
            if name in self.savings.keys():
                return self.savings[name]
        elif entrytype == "budget":
            if name in self.budgets.keys():
                return self.budgets[name]
        else:
            print("It seems that this entry doesn't exist! Maybe you made a typo?")


	#addItem(self)
    def additem(self):
        # Used to add items (can be savings, incomes, expenses, or budgets)
        print("Is this an:\n1. Income\n2. Saving\n3. Expense\n 4. Budget")
        choice = inputchecker(4)
        match choice:
            case 1:
                entrytype = "income"
            case 2:
                entrytype = "saving"
            case 3: 
                entrytype = "expense"
            case 4:
                entrytype = "budget"

        itemname = input("What is the name of this item:\n")
        print("What currency is this item in?:\n\n1. USD\n2. IRR\n3. EUR\n4. JPY\n5. GBP\n6. CHF\n7. CAD\n8. AUD\n9. SEK")
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

        itemscost = input("How much money was this item in the currency you inputted earlier (if saving, how much have you already saved)?:\n")
        itemscost = gummysint(itemscost)

        category = input("What is the category (ex: transport, entertainment, etc) of this item?:\n")

        if entrytype == "saving":
            saveamount = input("How much do you need to save?\n")
            saveamount = gummysint(saveamount)
        
        todaysday = datetime.datetime.now()

        if entrytype == "income":
            self.incomes[itemname] = Income(itemname, itemscost, currency, category, todaysday)
        elif entrytype == "saving":
            self.savings[itemname] = Saving(itemname, saveamount , currency, category, todaysday, itemscost)
        elif entrytype == "expense":
            self.expenses[itemname] = Expense(itemname, itemscost, currency, category, todaysday)
        elif entrytype == "budget":
            self.budgets[itemname] = BudgetEntry(itemname, itemscost, currency, category, todaysday)

        self.categories.append(category)

    def removeitem(self):
        # used to remove any entries not wanted
        print("Is this an:\n1. Income\n2. Saving\n3. Expense\n4. Budget")
        choice = inputchecker(4)
        match choice:
            case 1:
                entrytype = "income"
            case 2:
                entrytype = "saving"
            case 3: 
                entrytype = "expense"
            case 4:
                entrytype = "budget"

        itemname = input("What is the name of this item:\n")

        if entrytype == "income":
            self.incomes.pop(itemname)
            self.categories.remove(self.incomes[itemname]["category"].category)
        elif entrytype == "saving":
            self.savings.pop(itemname)
            self.categories.remove(self.savings[itemname]["category"].category)
        elif entrytype == "expense":
            self.expenses.pop(itemname)
            self.categories.remove(self.expenses[itemname]["category"].category)
        elif entrytype == "budget":
            self.budgets.pop(itemname)
            self.categories.remove(self.budgets[itemname]["category"].category)
        else:
            print("That item likely does not exist :(")

    def view_entries(self):
        # Used to view the selected kind of entry
        print("What kind of entry would you like to view?\n")
        print("1. Income\n2. Expenses\n3. Savings\n4.Budgets\n5. All Entries")

        choice = inputchecker(5)

        if choice == 1:
            incomeskeys = self.incomes.keys()
            for income in incomeskeys:
                print(self.incomes[income])
        elif choice == 2:
            expenses = self.expenses.keys()
            for expense in expenses:
                print(self.expenses[expense])
        elif choice == 3:
            savings = self.savings.keys()
            for saving in savings:
                print(self.savings[saving])
        elif choice == 4:
            budgets = self.budgets.keys()
            for budget in budgets:
                print(self.budgets[budget])
                self.ViewTotals(expenses=self.expenses, incomes=self.incomes)
        elif choice == 5:
            inclist = self.incomes.keys()
            explist = self.expenses.keys()
            savlist = self.savings.keys()
            budlist = self.budgets.keys()
            entries = []
            entries.extend(inclist)
            entries.extend(explist)
            entries.extend(savlist)
            entries.extend(budlist)

            for entry in entries:
                try:
                    print(self.expenses[entry])
                except:
                    try:
                         print(self.incomes[entry])
                    except:
                        try:
                            print(self.savings[entry])
                        except:
                            try:
                                print(self.budgets[entry])
                            except:
                                pass
                
        else:
            print("Invalid choice. Please try again.")

    class ViewTotals:
        # allows for the user to view totals for expenses and incomes
        def __init__(self, expenses, incomes):
            self.expenses = expenses
            self.incomes = incomes

        # Return a total of all the money in the selected category.

        def viewexpenses(self, totalamount=[]):
            for expense in self.expenses:
                flipexpense = expense.amount * -1
                totalamount.append(flipexpense)

            return sum(totalamount)

        def viewincomes(self, totalamount=[]):
            for income in self.incomes:
                totalamount.append(income.amount)
            
            return sum(totalamount)

        def viewall(self, totalamount=[], totalsubtract=[0]):
            for income in self.incomes:
                totalamount.append(income.amount)
            for expense in self.expenses:
                totalsubtract.append(expense.amount)
            
            return sum(totalamount) + sum(totalsubtract)

#class MoneyItem: (parent of income, expenses, saving, composition of currency)
class MoneyItem:
    ###explanation: this is a parent class to expenses, income, and savings
        ###it will take in 4 amounts name, amount held, currency it is in, and category.
#init there will be a couple of pieces of information.
    #1: Name
	#2: Amount
	#3: Currency
    #4: category
    def __init__(self, name, amount, currency, category, date):
        self.name = name
        self.amount = amount
        self.currency = currency
        self.category = category
        self.date = date
    
    def currchange(self):
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

        self.convert(currency)

    # Gets the currencies, and does unit conversions to get the new values
    def convert(self, new_currency):
        if self.currency != "USD":
            df = pd.read_csv("docs/currency.csv", skipinitialspace=True)
            rate = df.loc[df["currency"] == self.currency, "conversion to USD"].iat[0]
            self.amount *= rate
            print(df.loc[df["currency"] == self.currency, "conversion to USD"].iat[0])
            print(self.amount)
        
        df = pd.read_csv("docs/currency.csv", skipinitialspace=True)
        rate = df.loc[df["currency"] == new_currency, "conversion from USD"].iat[0]
        self.amount *= rate
        print(f"Conversion Rate: {df.loc[df["currency"] == new_currency, "conversion from USD"].iat[0]}")
        print(f"New Amount {self.amount:.2f} in {new_currency}")
        self.currency = new_currency


                

	

"""#class Currency: (aggregate of budget, child of money item)
class Currency: 
#init there will be the values name, conversion to USD, and the Conversion From USD
    def __init__(self, name, abreviation, conversion_to_USD, conversion_from_USD):
        self.name = name
        self.abreviation = abreviation
        self.conversion_to_USD = conversion_to_USD
        self.conversion_from_USD = conversion_from_USD

#def convert to usd(self, conversion_factor):
    def convertToUSD(self, conversion_factor):
	#Converted = Self.conversion to USD * conversion factor
        converted = self.conversion_to_USD * conversion_factor
	#return converted
        return converted

# def convert from usd(self, conversion_factor)
    def convertFromUSD(self, conversion_factor):
        #converted = self.conversion from USD *conversion_factor
        converted = self.conversion_from_USD * conversion_factor
    #return converted
        return converted"""


#class Income(MoneyItem):(aggregate of budget, child of money item)
class Income(MoneyItem):
#init will be the amount and name, use the super init function to get those.
#__str__:
    def __str__(self):
# f“Income: {self.name} made you {self.amount}” 
        return f"Income: {self.name} made you {self.amount} {self.currency}" 

#class Expense(MoneyItem)
class Expense(MoneyItem):
#init will be the amount and name, use the super init function to get those.
#__str__:
    def __str__(self):
# f“Expense: {self.name} cost you {self.amount}”
        return f"Expense: {self.name} cost you {self.amount}"


#class Saving(MoneyItem)(aggregate of budget, child of money item)
class Saving(MoneyItem):
#init will be the amount and name, use the super init function to get those, but this will have another variable called amount saved.
    def __init__(self, name, amount, currency, category, date, amount_saved):
        super().__init__(name, amount, currency, category, date)
        self.amount_saved = amount_saved
        self.amount_left = amount - amount_saved
        self.last_date_payed = ""

#pay:
    def pay(self):
        payment = floatInput(min=0.00, max = self.amount_left, prompt = f"\nEnter the amount you are paying, this should be a number from 0, to {self.amount_left}")
        self.amount_saved += payment
        self.amount_left -= payment
        print(self.__str__())
	#Self.amount_paid += amount_paid

#__str__: 
    def __str__(self):
        
        return f"{self.name} : Goal : {self.amount} | Amount Saved : {self.amount_saved} | Amount left to save : {self.amount_left} "
# f“Saving: You have saved {self.amount_saved} for Your goal,{self.name}, to raise {self.amount}” 

class BudgetEntry(MoneyItem):

    def __str__(self):
        return f"{self.name} | Your budget for this is {self.amount} {self.currency} | Category : {self.category} | Date : {self.date}"

    def budgetcheck(self, amount):
        if self.amount > amount:
            print(f"You are within your budget for {self.name}! You have {self.amount - amount} {self.currency} left to spend on this category!")
        elif self.amount == amount:
            print(f"You have exactly met your budget for {self.name}. Cutting it close!")
        else:
            print(f"You have exceeded your budget for {self.name} by {amount - self.amount} {self.currency}!")