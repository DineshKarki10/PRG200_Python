# Import the datetime module for working with dates and times
# datetime module provides classes for manipulating dates and times
from datetime import datetime, timedelta

# Global variable, defined outside any function
college_name = "Bhaktapur Multiple Campus"

# Function to convert a date string to a datetime object
# 'date_str' is a string in format 'YYYY-MM-DD' (e.g., "2025-05-01")
def parse_date(date_str):
    # datetime.strptime() parses a string into a datetime object
    # '%Y' = year with century (2025)
    # '%m' = month as number (05)
    # '%d' = day as number (01)
    # This converts "2025-05-01" to a datetime object
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    
    # Return the datetime object
    return date_obj

# Function to add days to a start date and return as a string
# 'start_str' is the start date as string 'YYYY-MM-DD'
# 'days' is the number of days to add (0, 3, 6, 10, 14)
def get_exam_date(start_str, days):
    # First, convert the start string to a datetime object
    start_date = parse_date(start_str)
    
    # Create a timedelta object representing 'days' number of days
    # timedelta is used to add or subtract time from a datetime
    delta = timedelta(days=days)
    
    # Add the timedelta to the start_date to get the exam date
    # This calculates: start_date + days
    exam_date = start_date + delta
    
    # Convert the datetime object back to a string in 'YYYY-MM-DD' format
    # strftime() formats a datetime as a string
    # %Y = year, %m = month, %d = day
    date_str = exam_date.strftime("%Y-%m-%d")
    
    # Return the formatted date string
    return date_str

# Function to print the complete exam schedule
def print_schedule(start_str, exams):
    # Use the global variable college_name
    print("-" * 50)
    print(college_name)
    print("EXAMINATION SCHEDULE")
    print("-" * 50)
    print()
    
    # Print the start date of the exams
    print("Exams start from: " + start_str)
    print("-" * 40)
    print()
    
    # Loop through each exam in the exams list
    # Each exam is a tuple: (subject, days)
    for subject, days in exams:
        # Get the exam date by calling get_exam_date()
        # This calculates: start_date + days
        exam_date = get_exam_date(start_str, days)
        
        # Print the subject and its exam date
        print(subject + ": " + exam_date)
    
    print()
    print("-" * 50)

# Given data: start date of the exams
start_date = "2025-05-01"

# List of exams with days to add from start date
# Each tuple has: (subject_name, days_to_add)
# 0 days = first exam on start date
# 3 days = 3 days after start date, etc.
exams = [
    ("Python Programming", 0),    
    ("Data Structures",    3),    
    ("Database Systems",   6),    
    ("Computer Networks",  10),   
    ("Mathematics",        14),  
]

# Call the print_schedule function with our data
print_schedule(start_date, exams)

# DEMONSTRATION OF LOCAL VARIABLE SCOPING
# The 'date_obj' variable inside parse_date() is LOCAL
# It only exists inside that function
# If we try to access it here (outside the function), we get an error

print("\n" + "-" * 50)
print("SCOPE DEMONSTRATION")
print("-" * 50)

# Try to access 'date_obj' outside the parse_date function
# This will cause a NameError because 'date_obj' is a local variable
# It was created inside parse_date() and doesn't exist here
try:
    # This line will cause an error because 'date_obj' doesn't exist here
    print(f"Trying to access 'date_obj' variable: {date_obj}")
except NameError:
    # The error message explains what happened
    print(" NameError: 'date_obj' is not defined in this scope")
    print(" Explanation: 'date_obj' is a LOCAL variable inside parse_date()")
    print(" It only exists within that function and cannot be accessed here")
