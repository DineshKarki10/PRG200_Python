# main.py ( This is the main program file)
# It imports and uses functions from the discount module

# Import specific items from the discount module
# 'final_price' is the function to calculate final price
# 'TAX_RATE' is the constant for tax rate
from discount import final_price, TAX_RATE

# List of products with their details
# Each tuple has: (product_name, original_price, discount_percentage)
products = [
    ("Laptop", 85000, 10),     
    ("Headphones", 4500, 15),   
    ("Phone Case", 800, 5),     
    ("USB Cable", 600, 0),      
]

# Printing
print("-" * 60)
print("SHOPPING CART - DISCOUNT & TAX CALCULATOR")
print("-" * 60)
print()

# Print the imported TAX_RATE to confirm it imported correctly
# This shows that we successfully imported from the discount module
print(f"Tax Rate: {TAX_RATE * 100}% VAT")
print("-" * 60)
print()

# Loop through each product in the products list
for product_name, price, discount_given in products:
    # Calculate the final price using the imported final_price function
    # This applies discount first, then adds tax
    final = final_price(price, discount_given)

    # Print the product details
    print(f"Product: {product_name}")
    print(f"Original Price: NPR {price}")
    print(f"Discount: {discount_given}%")
    print(f"Final Price: NPR {round(final, 2)}")  # Round to 2 decimal places
    print("-" * 40)

# DEMONSTRATION OF SCOPE WITH MODULES
# Variables defined inside functions in discount.py are LOCAL
# They cannot be accessed from main.py

print("\n" + "-" * 50)
print("SCOPE DEMONSTRATION")
print("-" * 50)

# Try to access a variable that only exists inside a function in discount.py
# 'discounted' is a LOCAL variable inside apply_discount()
# It doesn't exist in the global scope of discount.py, and definitely not here
try:
    # This will cause an error because 'discounted' is not defined here
    print(f"Trying to access 'discounted' variable: {discounted}")
except NameError:
    print(" NameError: 'discounted' is not defined in this scope")
    print(" Explanation: 'discounted' is a LOCAL variable inside apply_discount()")
    print(" It only exists within that function and cannot be accessed here")

# But TAX_RATE is GLOBAL in discount.py, so we can access it here
print("\n TAX_RATE is GLOBAL in discount.py and imported successfully:")
print(f" TAX_RATE = {TAX_RATE}")

