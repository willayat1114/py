# Input Weight & Height
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

# Calculation
b = weight/height

# Round Off
bmi = round(b, 2) 
print("BMI is: " , bmi)
