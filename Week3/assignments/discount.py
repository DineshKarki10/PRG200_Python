# Taking input from user
total = float(input("Enter the total purchase amount in NPR: "))
loyalty = input("Is the customer a loyalty program member? (yes/no): ").strip().lower()
payable_amt = 0

# Giving discounts based on total purchase amount
if total < 1000:
    payable_amt = total
elif total>=1000 and total < 5000:
    payable_amt = total - (total * 0.05)  # 5% discount
elif total >= 5000 and total < 15000:
    payable_amt = total - (total * 0.10)  # 10% discount
else:
    payable_amt = total - (total * 0.20)  # 20% discount

# Additional discount for loyalty program members
if loyalty == "yes":
    payable_amt -= (payable_amt * 0.05)  # Additional 5% discount

# Displaying the final amount to be paid
print(f"The amount to be paid is: NPR {payable_amt:.2f}")