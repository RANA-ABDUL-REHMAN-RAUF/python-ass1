# Take two numbers and an operator (+, -, *, /) as input and perform the corresponding operation.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

operator = input("Enter operator: ")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*" or operator == "x":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("Invalid operator")

print(f"{num1} {operator} {num2} = {result}")