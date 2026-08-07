# Import the math module that contains sqrt(), pow(), and many other math operations
import math

# Global variable - defined outside any function
# This variable can be accessed anywhere in the program
station_name = "Kathmandu Weather Station"

# Function to calculate the average (mean) of a list of temperatures
# 'temps' is a list of numbers (temperatures)
def get_average(temps):
    # Calculate the total sum of all temperatures in the list
    total = sum(temps)
    # Count how many temperatures are in the list
    count = len(temps)
    
    # Calculate the average by dividing total by count
    return total / count

# Function to calculate the standard deviation of temperatures
# Standard deviation measures how spread out the temperatures are
def get_deviation(temps):
    # First, calculate the mean (average) using get_average function
    # This is a LOCAL variable - only accessible inside this function
    mean = get_average(temps)
    
    # Create an empty list to store squared differences, calculate (temp - mean)²
    squared_diffs = []
    
    # Loop through each temperature in the list
    for temp in temps:
        # Calculate the difference between temp and mean
        diff = temp - mean
        # Square the difference (multiply it by itself)
        squared = diff * diff
        # Add the squared difference to our list
        squared_diffs.append(squared)
    
    # Calculate the variance
    variance = sum(squared_diffs) / len(squared_diffs)
    
    # Standard deviation is the square root of variance, math.sqrt() calculates the square root
    deviation = math.sqrt(variance)
    
    # Return the standard deviation
    return deviation

# Function to print a complete summary of the temperatures
# This function uses the global variable station_name
def get_summary(temps):
    # Use global variable station_name
    print(f"Weather Station: {station_name}")
    print("-" * 40)
    
    # Calculate the minimum temperature
    # min() finds the smallest number in the list
    min_temp = min(temps)
    
    # Calculate the maximum temperature
    # max() finds the largest number in the list
    max_temp = max(temps)
    
    # Calculate the average using our get_average function
    avg = get_average(temps)
    
    # Calculate the deviation using our get_deviation function
    dev = get_deviation(temps)
    
    # Print all the statistics
    print(f"Minimum Temperature: {min_temp}°C")
    print(f"Maximum Temperature: {max_temp}°C")
    print(f"Average Temperature: {round(avg, 2)}°C")
    print(f"Standard Deviation: {round(dev, 2)}")
    print("-" * 40)

# Create a list of temperature readings, given data
temperatures = [18.4, 22.1, 15.7, 29.3, 11.8, 25.6, 19.2]

# Call the get_summary function with our temperature data
get_summary(temperatures)


# DEMONSTRATION OF LOCAL VARIABLE SCOPING
# The 'mean' variable inside get_deviation() is LOCAL
# It only exists inside that function
# If we try to access it here (outside the function), we get an error

print("\n" + "-" * 50)
print("SCOPE DEMONSTRATION")
print("-" * 50)

# Try to access 'mean' outside the function
# This will cause a NameError because 'mean' is a local variable
# It was created inside get_deviation() and doesn't exist here
try:
    # This line will cause an error
    print(f"Trying to access 'mean' variable: {mean}")
except NameError:
    # The error message explains what happened
    print(" NameError: 'mean' is not defined in this scope")
    print("   Explanation: 'mean' is a LOCAL variable inside get_deviation()")
    print("   It only exists within that function and cannot be accessed here")

