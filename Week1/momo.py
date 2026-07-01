# inputs
cost_per_plate = float(input("Enter the cost per plate of the momo :"))
sold_per_plate = float(input("Enter the selling price per plate: "))
unit_sold = int(input("Enter the total number of plates sold: "))
# Totals
total_rev = sold_per_plate*unit_sold
total_cost = cost_per_plate*unit_sold
# Profit and profit margin
total_profit = total_rev - total_cost
profit_margin = (total_profit/total_rev)*100
# Outputs 
print((f"Total Revenue Genarated: {total_rev}"))
print((f"Total Cost : {total_cost}"))
print((f"Total Profit : {total_profit}"))
print((f"Profit Margin : {profit_margin} % "))
