incomelist = []
expenselist = []
expenseamt = []
transactions  = 0
balance = 0 

def trackerRun():
    global balance, transactions
    while True:
        type = input("Enter transaction type (Income/Expense) or 'exit' or 'view balance' or 'view transaction history': ")
        if type == "exit":
           exit()
        elif type == "Expense":
           addTransaction()
           continue
        elif type == "Income":
           addIncome()
           continue
        elif type == "view balance":
            viewBalance()
            continue
        elif type == "view transaction history":
            viewTransactionHistory()
            continue
        else:
           trackerRun()

      
def addIncome():
    global balance, transactions
    amount = int(input("Please enter the amount that you have earned: $"))
    balance += amount
    type = input("What is the category?: ")
    incomelist.append(type)

def addTransaction():
    global balance, transactions
    amount = int(input("Please enter the amount that you have spent: $"))
    balance -= amount 
    expenseamt.append(amount)
    type = input("What is the category?: ")
    expenselist.append(type)
    transactions+=1

def viewBalance():
    global balance, transactions
    view = input("Would you like to view balance?: ")
    if view == "yes":
        print("You have a balance of $", balance)
    


def viewTransactionHistory():
    global balance, transactions
    for i in range (transactions):
        print(expenselist[i],"$",expenseamt[i])
  

trackerRun()
