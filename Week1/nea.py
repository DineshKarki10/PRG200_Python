previous_meter = float(input("Enter the previous month meter reading: "))
current_meter = float(input("Enter the current month reading: "))
consumed_unit = current_meter-previous_meter

# Calculating comsumption price, NRP 13 per unit
consumed_amt = 13*consumed_unit

# final amt with monthly service charge of NRP 10
final_amt = consumed_amt + 10

# output
print((f"Total Bill : {final_amt}"))