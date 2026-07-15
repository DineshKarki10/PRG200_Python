def estimate_fare(distance_km, vehicle_type, surge=1.0):
    base_fare = 0
    if vehicle_type == "Car":
        base_fare = 10
    elif vehicle_type == "Bike":
        base_fare = 5
    else:
        return "Invalid vehicle type"
    
    fare = base_fare * distance_km * surge
    return fare

vechicle_type = input("Enter vehicle type (Car/Bike): ")
distance = float(input("Enter distance in kilometers: "))
fare = estimate_fare(distance, vechicle_type)
print(fare)