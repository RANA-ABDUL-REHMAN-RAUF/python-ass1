# Ask the user for a grade percentage and display the corresponding letter grade (A, B, C, D, F).

grade = int(input("Enter your grade percentage: "))
if grade >= 90:
    print("Your grade is A")
elif grade >= 80:
    print("Your grade is B")
elif grade >= 70:
    print("Your grade is C")
elif grade >= 60:
    print("Your grade is D")
elif grade >= 33:
    print("Your grade is E")
else:
    print("Your grade is F")