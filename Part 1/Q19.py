# Check if a string input is uppercase, lowercase, or a mix.
input= input("Enter a string: ")
if input.isupper():
    print("Uppercase")
elif input.islower():
    print ("Lowercase")
else: 
    print("Mix")