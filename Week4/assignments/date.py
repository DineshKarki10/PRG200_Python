# Create a function convert_date() that takes three parameters (date_str, from_cal, to_cal)
def convert_date(date_str, from_cal, to_cal):
    
    # If same calendar, return the date unchanged
    if from_cal == to_cal:
        return date_str
    
    # Split the date into year, month, day
    parts = date_str.split("-")
    year = int(parts[0])
    month = int(parts[1])
    day = int(parts[2])
    
    # Convert based on data
    if from_cal == "AD" and to_cal == "BS":
        # AD to BS: Add 56 to year
        new_year = year + 56
    elif from_cal == "BS" and to_cal == "AD":
        # BS to AD: Subtract 56 from year
        new_year = year - 56
    else:
        # This should not happen if input is valid
        return date_str
    
    # Format the new date
    new_date = str(new_year) + "-" + str(month).zfill(2) + "-" + str(day).zfill(2)
    
    return new_date

# Calling,and printing the function
print(convert_date("1985-06-24", "AD", "BS")) 
print(convert_date("2055-09-10", "BS", "AD"))  