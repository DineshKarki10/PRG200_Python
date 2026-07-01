# Taking inputs
person1 = float(input("Enter First person's contribution amount :"))
person2 = float(input("Enter Second person's contribution amount :"))
person3 = float(input("Enter Third person's contribution amount :"))
# total exp
total_exp = person1+person2+person3
# divided amt
divided_ampt = total_exp/3
# Outputs
print((f"Total Trip Expense: {total_exp}"))
print((f"Each person has to contribute: {divided_ampt}"))
print((f"First person has contrubuted {person1 - divided_ampt}"))
print((f"Second person has contrubuted {person2 - divided_ampt}"))
print((f"Third person has contrubuted {person3 - divided_ampt}"))