# Write a program that checks if a given number is positive, negative, or zero.
input= int(input("Enter a number: "))
if input == 0:
    print(f"{input} is zero")
elif input > 0: 
    print(f"{input} is positive")
else:
    print(f"{input} is negative")