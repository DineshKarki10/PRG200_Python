# List of passwords to check 
passwords = ["hello", "Hello123", "H3ll0@World", "12345678", "MyP@ss!"]

# The required special charatcters 
special_chars = "!@#$%^&*"

# Checking each password for strength
for pwd in passwords:
    # List to keep track of missing criteria 
    missing = []
    # Checking the length of the password
    if len(pwd) < 8:
        missing.append("At least 8 characters long")
    # Checking for uppercase letters
    if not any(ch.isupper() for ch in pwd):
        missing.append("At least one uppercase letter")
    # Checking for lowercase letters
    if not any(ch.islower() for ch in pwd):
        missing.append("At least one lowercase letter")
    # Checking for digits
    if not any(ch.isdigit() for ch in pwd):
        missing.append("At least one digit")
    # Checking for special characters
    if not any(ch in special_chars for ch in pwd):
        missing.append("At least one special character (!@#$%^&*)")
    
    # Disaplaying the final result 
    if missing:
        print(f"{pwd} is WEAK. Missing: {', '.join(missing)}")
    else:
        print(f"{pwd} is STRONG , meets all criteria!! ")