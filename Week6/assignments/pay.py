# Import the random module for picking a random friend
# random module provides functions for generating random numbers and choices
import random

# Set a fixed seed so the results are consistent every time you run the program
# This ensures the "random" choice is always the same for testing purposes
# Without this, the lucky person would change each time
random.seed(42)

# Function to split the bill equally among all friends
# 'friends' is a list of friend names
# 'total' is the total bill amount
def split_bill(friends, total):
    # Calculate how many friends there are
    count = len(friends)
    # Calculate the amount each person pays (equal split)(local variable)
    share = total / count 
    # Return the per-person share
    return share

# Function to randomly pick one lucky person
def pick_lucky(friends):
    # random.choice() picks one random item from the list(local variable)
    lucky = random.choice(friends)
    # Return the name of the lucky person
    return lucky

# Function to print the final summary of the bill
def final_summary(friends, total):
    # Call split_bill() to get the equal share amount(local variable)
    share = split_bill(friends, total)
    # Call pick_lucky() to get the lucky person's name(local variable)
    lucky_person = pick_lucky(friends)
    
    # Calculate the lucky person's total (share + extra 50)(local variable)
    lucky_total = share + 50
    
    # Printing
    print("-" * 40)
    print("BILL SPLITTER - THAMEL RESTAURANT")
    print("-" * 40)
    print()
    
    # Print each person's share
    print("Each person's share:")
    print("-" * 25)
    
    # Loop through each friend in the list
    for person in friends:
        # Check if this person is the lucky one
        if person == lucky_person:
            print(f"{person}: NPR {round(lucky_total, 2)} (includes NPR 50 tax)")
        else:
            # Normal person pays just their share
            print(f"{person}: NPR {round(share, 2)}")
    
    print()
    print("-" * 40)
    
    # Print the lucky person details
    print(f" Lucky Person: {lucky_person} pays extra NPR 50!")
    print(f" {lucky_person} pays: NPR {round(lucky_total, 2)}")
    
    print()
    print("-" * 40)


# Given data: list of friends
friends = ["Ramesh", "Sunita", "Bikash", "Anjali", "Dipak"]

# Total bill amount
total_bill = 3750

# Call the final_summary function with given data
final_summary(friends, total_bill)

# DEMONSTRATION OF LOCAL VARIABLE SCOPING
# The 'share' variable inside split_bill() is LOCAL
# It only exists inside that function
# If we try to access it here (outside the function), we get an error

print("\n" + "-" * 50)
print("SCOPE DEMONSTRATION")
print("-" * 50)

# Try to access 'share' outside the split_bill function
# This will cause a NameError because 'share' is a local variable
# It was created inside split_bill() and doesn't exist here
try:
    # This line will cause an error because 'share' doesn't exist here
    print(f"Trying to access 'share' variable: {share}")
except NameError:
    # The error message explains what happened
    print(" NameError: 'share' is not defined in this scope")
    print(" Explanation: 'share' is a LOCAL variable inside split_bill()")
    print(" It only exists within that function and cannot be accessed here")

    