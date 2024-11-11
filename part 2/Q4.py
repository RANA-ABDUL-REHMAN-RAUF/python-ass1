# Print the multiplication table of a given number.
input= int(input("Enter a number: "))
for i in range(1,11):
    result=  i*input
    print(f"{input} x {i} = {result}")