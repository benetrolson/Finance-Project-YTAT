
#explanation: used by other input functions
def userInput(prompt = '> '):
    return input(prompt).lower().strip()


#explanation: allows user to input a number of their choice, you can set the max and min, the number they type will have to be between those [the max and min are INCLUDED!]
def intInput(max = 100000,prompt='> ',min = 0):
    while True:
        num = userInput(prompt)
        try:
            num = int(num)
        except:
            print('\nInput is not a number!')
            continue
        if num <= max and num >= min:
            return num
        else:
            print('\nInput is out of range!')


#Explanation: same as int input but with a float!
def floatInput(max = 100000.00,prompt='> ',min = 0.00):
    while True:
        num = userInput(prompt)
        try:
            num = float(num)
        except:
            print('\nInput is not a number!')
            continue
        if num <= max and num >= min:
            return num
        else:
            print('\nInput is out of range!')

#explanation: choice input allows tyou to select a choice. choices should be equal to a list... IE: bats = choiceInput(['big','small','medium'], "What size bat would you like?") the user will then be asked what bat they like till they enter one of the things in that list
def choiceInput(choices,prompt = '> '):
    while True:
        choice = userInput(prompt)
        if choice in choices:
            return choice
        else:
            print('\nPlease select a valid choice!')