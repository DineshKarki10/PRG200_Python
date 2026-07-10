# Inputs 
no_of_trekers = int(input("Enter the number Trekers: "))
ACAP_TIMS_charge = float(input("Enter the sum of ACAP permit charge and TIMS charge: "))

# Total Cost
total_cost = no_of_trekers* ACAP_TIMS_charge
print(f"Total Cost : {total_cost}")

# 5% service charge
service = (5/100)*total_cost
print(f"5% service charge: {service}")
print(f"Total Cost with 5% service charge: {service + total_cost}")

# Cost per person with 5% service charge 
total_amt = (service+total_cost)/no_of_trekers
print(f"Total Cost per person with 5% service charge: {total_amt}")
