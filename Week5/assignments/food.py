# Define the parent class (DeliveryClass)
class DeliveryPartner:
    # __init__ runs when we create any delivery partner object
    def __init__(self, name, partner_id, deliveries):
        self.name = name
        self.partner_id = partner_id
        self.deliveries = deliveries
    
    # This method is meant to be overridden by child classes (calculates total earnings)
    def total_earning(self):
        return 0
    
    # This method displays the partner's information
    def display(self):
        print("Name: " + self.name + " (" + self.partner_id + ")")
        print("Deliveries: " + str(self.deliveries))
        # Calculate earnings by calling total_earning()
        earning = self.total_earning()
        print("Total Earnings: NPR " + str(earning))
        print("-" * 30)

# Define the BikeRider class - inherits from DeliveryPartner
class BikeRider(DeliveryPartner):
    # # __init__ takes all parent parameters and km_travelled
    def __init__(self, name, partner_id, deliveries, km_travelled):
        DeliveryPartner.__init__(self, name, partner_id, deliveries)
        self.km_travelled = km_travelled
    
    # Override the total_earning method from parent
    def total_earning(self):
        # Calculate: (deliveries × 80) + (km_travelled × 5)
        earning = (self.deliveries * 80) + (self.km_travelled * 5)
        return earning

# Define the Walker class - inherits from DeliveryPartner
class Walker(DeliveryPartner):
    # __init__ takes parent parameters and rainy_deliveries
    def __init__(self, name, partner_id, deliveries, rainy_deliveries):
        DeliveryPartner.__init__(self, name, partner_id, deliveries)
        self.rainy_deliveries = rainy_deliveries
    
    # Override the total_earning method for Walker
    def total_earning(self):
        # Calculate: (deliveries × 60) + (rainy_deliveries × 50)
        earning = (self.deliveries * 60) + (self.rainy_deliveries * 50)
        return earning

# Define the CarDriver class - inherits from DeliveryPartner
class CarDriver(DeliveryPartner):
    # __init__ takes parent parameters and fuel_cost
    def __init__(self, name, partner_id, deliveries, fuel_cost):
        DeliveryPartner.__init__(self, name, partner_id, deliveries)
        self.fuel_cost = fuel_cost
    
    # Override the total_earning method for CarDriver
    def total_earning(self):
        # Calculate: (deliveries × 120) - fuel_cost
        earning = (self.deliveries * 120) - self.fuel_cost
        return earning

# Create a list of partner objects
partners = [
    BikeRider("Santosh Rai", "B-01", 15, 42),
    Walker("Kabita Maharjan", "W-01", 18, 5),
    CarDriver("Roshan KC", "C-01", 20, 850),
]

# Print 
print("-" * 30)
print("DELIVERY PARTNERS")
print("-" * 30)
print()

# Loop through each partner in the partners list
for partner in partners:
    partner.display()
    print() 

# Find the partner with the highest earning
highest_earner = partners[0]

# Loop through each partner in the partners list
for partner in partners:
    if partner.total_earning() > highest_earner.total_earning():
        highest_earner = partner

# Print the partner with the highest earning
print("-" * 30)
print("HIGHEST EARNING PARTNER:")
print("-" * 30)
# Call display() on the highest earner 
highest_earner.display()
