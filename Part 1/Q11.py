# Write a program that takes a temperature in Celsius and checks if it’s freezing, moderate, or hot.
temp = input("Enter the temperature in Celsius: ")

if temp < 0:
    print("Freezing")
elif temp >= 0 and temp < 10:
    print("Moderate")
else:
    print("Hot")