store_name = []
product_name = []
product_price = []

for i in range(2):
    store_name.append(input(f"Enter the name of store {i + 1}: "))
    product_name.append(input(f"Enter the name of product {i + 1}: "))
    product_price.append(float(input(f"Enter the price of product {i + 1}: ")))

print("\nPrice from Lowest Price to Highest Price:")
print(sorted(product_price))

highest_price = product_price[0]
lowest_price = product_price[-1]
print(f"Highest Price: {highest_price}")
print(f"Best Store (Lowest Price): {lowest_price}")

average_price = sum(product_price) / len(product_price)
print(f"\nAverage Price: {average_price}")

print("\nIf Purchased from the best store, you will save:")
savings = highest_price - lowest_price
print(f"\nSavings if Purchased from Best Store: {savings}")

delivery = input("\nDoes the cheapest store charge delivery? (yes/no): ")

if delivery.lower() == "yes":
    charge = float(input("\nEnter delivery charge: "))
    final_price = lowest_price + charge
else:
    charge = 0
    final_price = lowest_price

print("\nDelivery Charge:", charge)
print("Final Cost:", final_price)