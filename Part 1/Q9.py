# Take three sides of a triangle as input and check if they form a valid triangle.
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a + b > c and b + c > a and c + a > b:
    print("Valid triangle")
else:
    print("Invalid triangle")