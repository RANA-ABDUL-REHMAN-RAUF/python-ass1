#  Print the reverse of a given number.
num = int(input("Enter an integer to reverse: "))
reverse = 0
temp = num
while temp > 0:
    reverse = (reverse * 10) + (temp % 10)
    temp //= 10
print("Reversed number:", reverse)