# Create the function check_water_level() that takes two parameters (location and level_metres)
def check_water_level(location, level_metres):
    
    # Check if water level is below 3 metres
    if level_metres < 3:
        return "Safe"
    
    # Check if water level is between 3 and 5 metres
    elif level_metres >= 3 and level_metres < 5:
        return "Warning — Alert nearby villages"
    
    # If level is above 5 metres
    else:
        return "DANGER — Evacuate immediately!"

# Given data list
sensors = [
    ("Chatara", 2.8),
    ("Tribeni Ghat", 5.4),
    ("Koshi Barrage", 4.1),
    ("Sunsari Bridge", 1.9),
    ("Saptakoshi Camp", 6.0),
]

# Print header
print("  KOSHI RIVER WATER LEVEL ALERT SYSTEM ")
print()

# Go through each value
for location, level in sensors:
    # Get the alert level
    alert = check_water_level(location, level)
    
    # Display the result
    print(f"{location} ({level} m): {alert}")