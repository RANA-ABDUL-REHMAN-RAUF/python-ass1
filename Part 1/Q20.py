# Create a program that evaluates if an inputted number is prime.

num = int(input("Enter a number: "))

for i in range(2, num):
    if num % i == 0:
        print(f"{num} is not a  prime number")
        break
else:
    print(f"{num} is a prime number")