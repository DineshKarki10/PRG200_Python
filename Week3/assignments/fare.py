# Trip distance and hour data   
trips = [
    {"distance": 1.5, "hour": 14},
    {"distance": 5.0, "hour": 22},
    {"distance": 12.0, "hour": 3},
    {"distance": 8.5, "hour": 10},
    {"distance": 2.0, "hour": 23},
]

# Calculating fare for each trip
for trip in trips:
    distance = trip["distance"]
    hour = trip["hour"]
    
    # Base fare calculation
    if distance <= 2:
        fare = 150
    elif distance <= 10:
        fare = 150 + (distance - 2) * 35
    else:
        fare = 150 + 8 * 35 + (distance - 10) * 28
    
    # Apply night surcharge (10 PM – 5 AM)
    is_night = (hour >= 22) or (hour < 5)
    if is_night:
        fare *= 1.10  # 10% extra
    
    # Round to 2 decimal places
    fare = round(fare, 2)
    
    # Displaying the final output
    print(f"Distance: {distance} km, Hour: {hour}:00, Fare: NPR {fare}")

    