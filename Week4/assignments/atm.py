# Create the function atm() that takes account_id, pin, action, and amount as parameters
def atm(account_id, pin, action, amount=0):
   
    # Account data
    accounts = {
        "A001": {"name": "Ramesh Thapa",  "balance": 15000, "pin": "1234"},
        "A002": {"name": "Sunita Karki",  "balance": 8500,  "pin": "5678"},
        "A003": {"name": "Bikash Rai",    "balance": 22000, "pin": "9012"}
    }
    
    # Check if account exists
    if account_id not in accounts:
        print("Account not found")
        return
    
    # Check if PIN matches
    if accounts[account_id]["pin"] != pin:
        print("Incorrect PIN")
        return
    
    # Get account details
    name = accounts[account_id]["name"]
    balance = accounts[account_id]["balance"]
    
    # Perform the action
    if action == "balance":
        # Show balance
        print(f"{name} — Balance: NPR {balance}")
    
    elif action == "deposit":
        # Deposit money
        new_balance = balance + amount
        accounts[account_id]["balance"] = new_balance
        print(f"{name} deposited NPR {amount}")
        print(f"New balance: NPR {new_balance}")
    
    elif action == "withdraw":
        # Withdraw money
        if amount > balance:
            print("Insufficient funds")
        else:
            new_balance = balance - amount
            accounts[account_id]["balance"] = new_balance
            print(f"{name} withdrew NPR {amount}")
            print(f"New balance: NPR {new_balance}")
    
    else:
        print("Invalid action")

# Testing the function with given data 
print("ATM SIMULATOR")
print()

# Test Case 1: Check balance (correct PIN)
print("TEST 1: Balance check")
atm("A001", "1234", "balance")
print()

# Test Case 2: Wrong PIN
print("TEST 2: Wrong PIN")
atm("A002", "0000", "withdraw", 2000)
print()

# Test Case 3: Deposit
print("TEST 3: Deposit")
atm("A002", "5678", "deposit", 3000)
print()

# Test Case 4: Insufficient funds
print("TEST 4: Insufficient funds")
atm("A003", "9012", "withdraw", 25000)
print()

# Test Case 5: Account not found
print("TEST 5: Account not found")
atm("A004", "1111", "balance")