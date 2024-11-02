# Write a program to determine if a given character is a vowel or consonant.
letter= input("Enter a character: ")
letter= letter.lower()
if letter in "aeiou":
    print (f"{letter} is a vowel")
elif letter.isalpha() :
    print(f"{letter} is a consonant")
else:
    print(f"{letter} is not a vowel or a consonant")