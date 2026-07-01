# Inputs
basic_salary = float(input("Enter the monthly basic salary in NRP: "))
deduction_precenntage = float(input("Enter the monthly deduction :"))

# Calculate deduction 
deduct = (deduction_precenntage/100)*basic_salary
after_deduct = basic_salary - deduct
print(f"Your deduction : {after_deduct}")

# Bonus + after deduction amount 
final_amt = basic_salary + after_deduct

# Output
print(f"You will get NRP. {final_amt} in hand with Dashanin Bonus after deductions ")