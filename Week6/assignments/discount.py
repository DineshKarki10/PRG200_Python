# discount.py, custom module for discount calculations

# Global constant for tax rate (13% VAT)
TAX_RATE = 0.13

# Function to apply a discount percentage to a price
def apply_discount(price, percent):
    # Calculate the discount amount
    discount = price * (percent / 100)

    # Subtract discount from price to get the discounted price
    discounted = price - discount
    
    # Return the price after discount
    return discounted

# Function to add tax to a price
# 'price' is the price before tax
def apply_tax(price):
    # Calculate the tax amount using the global TAX_RATE
    tax = price * TAX_RATE

    # Add tax to the price
    total = price + tax
    
    # Return the price including tax
    return total

# Function to calculate final price (discount first, then tax)
# 'price' is the original price
# 'discount_pct' is the discount percentage
def final_price(price, discount_pct):
    # First, apply the discount to get the discounted price
    after_discount = apply_discount(price, discount_pct)
    
    # Then, apply tax to the discounted price
    final = apply_tax(after_discount)
    
    # Return the final price (discount applied first, then tax)
    return final

