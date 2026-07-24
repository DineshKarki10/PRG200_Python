# Create the function process_order() that takes two parameters( inventory and cart)
def process_order(inventory, cart):
    # Create a variable to keep track of the total bill
    total = 0
    
    # Printing the Bill header
    print("---- Bill ----")
    
    # Loop through each item in the cart
    for item in cart:
        # Check if we have enough stock
        if inventory[item]["stock"] >= cart[item]:
            # Calculate: price * quantity
            item_total = inventory[item]["price"] * cart[item]
            
            # Add to total bill
            total = total + item_total
            
            # Reduce the stock
            inventory[item]["stock"] = inventory[item]["stock"] - cart[item]
            
            # Print the bill line
            # Convert numbers to string using str() so we can add them
            print(f"{item} x{cart[item]} = NPR {item_total}")
        else:
            # If not enough stock, print this message
            print(f"Sorry, not enough stock for {item}")
    
    # Printing the grand total
    print(f"Grand Total: NPR {total}")
    print("--------------")
    
    # Printing the updated inventory
    print(f"Updated stock: rice={inventory['rice']['stock']}, milk={inventory['milk']['stock']}, bread={inventory['bread']['stock']}, eggs={inventory['eggs']['stock']}")
   


# Given DATA
inventory = {
    "rice":  {"price": 120, "stock": 20},
    "milk":  {"price": 90,  "stock": 10},
    "bread": {"price": 60,  "stock": 15},
    "eggs":  {"price": 15,  "stock": 30}
}

cart = {
    "rice": 2,
    "milk": 3,
    "eggs": 12
}

# Calling the function
process_order(inventory, cart)
