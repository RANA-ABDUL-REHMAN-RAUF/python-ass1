
#  Write a program that continues to ask for a number until the correct number is guessed.
secret_number = 7
while True:
    guess = int(input("Guess the number: "))
    if guess == secret_number:
        print("Correct! You guessed the number.")
        break
    else:
        print("Try again.")
