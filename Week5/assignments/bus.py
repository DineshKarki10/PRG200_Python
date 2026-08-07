# Define the Bus class
class Bus:
    # __init__ runs when we create a new bus object
    def __init__(self, route, total_seats):
        self.route = route
        self.total_seats = total_seats
        # Create an empty list to store booked seats
        # Each booking will be a tuple: (seat_number, passenger_name)
        self.booked = []
    
    # Method to book a seat for a passenger
    def book_seat(self, seat_number, passenger_name):
        # Check if the seat number is valid (between 1 and total_seats)
        if seat_number < 1 or seat_number > self.total_seats:
            print("Invalid seat number")
            return
        
        # Loop through all bookings in the booked list
        for booking in self.booked:
            # Check if this booking has the same seat number
            if booking[0] == seat_number:
                print("Seat already booked")
                return 
        
        # If seat is available
        # Create a tuple with seat number and passenger name
        booking = (seat_number, passenger_name)
        # Add the booking to the booked list
        self.booked.append(booking)
        print("Seat " + str(seat_number) + " booked for " + passenger_name)
    
    # Method to count how many seats are still available
    def available_seats(self):
        available = self.total_seats - len(self.booked)
        return available
    
    # Method to display all booked seats with passenger names
    def passenger_list(self):
        print("Passenger List for " + self.route)
        print("-" * 35)
        
        if len(self.booked) == 0:
            # If no bookings, print this message
            print("No passengers booked yet")
        else:
            # Loop through each booking in the booked list
            for booking in self.booked:
                # booking[0] is the seat number
                # booking[1] is the passenger name
                print("Seat " + str(booking[0]) + ": " + booking[1])
        
        print("-" * 35)

# Create a new Bus object, Route: "Kathmandu - Pokhara", Total seats: 10
bus = Bus("Kathmandu - Pokhara", 10)

# Create a list of bookings
bookings = [
    (3, "Ramila Shrestha"),   # Book seat 3 for Ramila
    (7, "Deepak Gurung"),     # Book seat 7 for Deepak
    (3, "Anita Rai"),         # Try to book seat 3 again (duplicate - should fail)
    (1, "Prakash Magar"),     # Book seat 1 for Prakash
    (7, "Suman Tamang"),      # Try to book seat 7 again (duplicate - should fail)
]

# Print
print("-" * 40)
print("SAJHA YATAYAT BUS BOOKING")
print("-" * 40)
print()

# Loop through each booking in the bookings list
for seat, name in bookings:
    # Call book_seat() method for each booking
    bus.book_seat(seat, name)
print()  

# Print how many seats are still available, Call available_seats() method
available = bus.available_seats()
print("Available seats: " + str(available))
print() 

# Print the full passenger list, Call passenger_list() method
bus.passenger_list()

print()  
print("-" * 40)
print("BOOKING COMPLETE")
print("-" * 40)