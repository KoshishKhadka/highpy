import random

secret_number = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))
guess_count = 1

while guess != secret_number:
    if guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
    guess = int(input("Guess again: "))
    guess_count += 1

print(f"Correct! You got it in {guess_count} guesses!")