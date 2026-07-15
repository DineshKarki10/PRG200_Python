orders = [("Book", 5), ("Phone", 2), ("Shoes", 7), ("Laptop", 1)]
orders.sort(key=lambda x: x[1])

print(orders)