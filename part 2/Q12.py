#  Print all prime numbers between 1 and 50.
print("Prime numbers between 1 and 50 are:")
for num in range(2, 51):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()

