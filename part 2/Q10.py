# 1. Use a loop to count the number of digits in an integer.
num = int(input("Enter an integer: "))
count = 0
temp = num
while temp != 0:
    temp //= 10
    count += 1
print("Number of digits:", count)