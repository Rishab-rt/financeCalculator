incomelist = []
expenselist = []
expenseamt = []
incomeAmt = []
transactions = 0
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
    incomeAmt.append(amount)
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
        print(f"You have a balance of ${balance}")
    


def viewTransactionHistory():
    global balance, transactions
    for i in range (transactions):
        print(f"{expenselist[i]}${expenseamt[i]}")

def averageTransactions():
    global balance, transactions
    average = sum(expenseamt)/transactions
    print(f"You have spent on average ${average} per transaction for the last {len(expenseamt)} transactions")

def incomeHistory():
    global balance, transactions
    for i in range (len(incomeAmt)):
        print(f"{incomelist[i]}${incomeAmt[i]}")

def generateSummary():
    global balance, transactions
    viewBalance()
    averageTransactions()
  

trackerRun()
