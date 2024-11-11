#  Create a program to calculate the sum of the digits of an inputted integer.
num = int(input("Enter an integer: "))
sum_of_digits = 0
temp = num
while temp > 0:
    sum_of_digits += temp % 10
    temp //= 10
print("Sum of digits:", sum_of_digits)
