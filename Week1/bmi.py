# Inputs 
weight = float(input("Enter your weight in Kg: "))
height = float(input("Enter your height in cm: "))

# converting cm into m
height_in_meters = height/100

# calculating BMI
bmi = weight/(height_in_meters**2)
round_bmi = round(bmi,1)

# Output
print(f"Your BMI is {round_bmi}")