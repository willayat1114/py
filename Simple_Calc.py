# Simple Calculator

# Input Numbers
num1 = float(input("Enter first value: "))
num2 = float(input("Enter second value"))

# Input Operations

op = input("Enter any of the following operations [+, -, *, /]")

# Define Operations

if op == "+":
    result = num1+num2
elif op == "-":
    result = num1-num2
elif op == "*":
    result = num1*num2
elif op == "/":
    result = num1/num2
else:
    print("Wrong Input, Program Terminated")

print("The result is", result)
