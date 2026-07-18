# Taking inputs from the user
balance = float(input("Enter your current balance in NPR: "))
daily_withdrawal = float(input("Enter the amount you have already withdrawn today in NPR: "))
amount = float(input("Enter the amount you want to withdraw in NPR: "))

# Checking if the withdrawal amount is sufficient, or not
if amount <= balance:
    # Checking if the withdrawal amount is a multiple of 500
    if amount % 500 == 0:
        # Checking if the user has reached the daily withdrawal limit
        if daily_withdrawal < 50000:
            # Checking if the total daily withdrawal + amount exceeds the limit
            if daily_withdrawal + amount <= 50000:
                # Subtracting the withdrawal amount from the balance
                balance -= amount
                # Updating the daily withdrawal amount
                daily_withdrawal += amount
                # Success message for successful withdrawal
                print("Withdrawal successful!!")
                # Displaying the current balance after withdrawal
                print(f"Your current balance after withdrawal: NPR {balance}")
            else:
                # Message for exceeding daily withdrawal limit when current amount is withdrawn
                print("With your current withdrawal, you will exceed your daily withdrawal limit of NPR 50,000.")
        else:
            # Message for exceeding daily withdrawal limit
            print("You have reached your daily withdrawal limit of NPR 50,000.")
    else:
        # Message for invalid withdrawal amount i.e. not a multiple of 500
        print("Invalid withdrawal amount. Please enter a multiple of 500.")
else:
    # Message for insufficient balance
    print("Insufficient balance.")