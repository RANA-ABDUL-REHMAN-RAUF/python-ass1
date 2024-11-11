#  Print the sum of even and odd numbers separately up to a given number.
limit = int(input("Enter the limit: "))
even_sum, odd_sum = 0, 0
for i in range(1, limit + 1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
