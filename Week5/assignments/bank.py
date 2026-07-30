# Define the class, BankAccount
class BankAccount:
    # Storing the objects, init to automalically creating an object
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    # deposit function 
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(self.name + " deposited NPR " + str(amount))
        print("New balance: NPR " + str(self.balance))

    # Withdrawal function
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance = self.balance - amount
            print(self.name + " withdrew NPR " + str(amount))
            print("New balance: NPR " + str(self.balance))

    # Balance check function
    def get_balance(self):
        print(self.name + " — Balance: NPR " + str(self.balance))

# Create accounts
accounts = [
    BankAccount("Ramesh Thapa", "A001", 5000),
    BankAccount("Sunita Karki", "A002", 0),
    BankAccount("Bikash Rai", "A003", 12000)
]

# Do transactions
accounts[1].deposit(3000)      # Sunita deposits
accounts[2].withdraw(15000)    # Bikash tries (fails)
accounts[0].withdraw(2000)     # Ramesh withdraws

# Show final balances
print("\nFinal Balances:")
for acc in accounts:
    acc.get_balance()
