# A guessing game
from random import randint


# Create a function
def guessing_game():
    """Generates a random number from 0 to 10 and compares it with the user's input"""
    random_number = randint(0, 10)
    # Create an indefinite loop
    while True:
        guess = int(input("Guess the number: "))
        if guess > random_number:
            print(f"Your guess of {guess} is too High!")
        elif guess < random_number:
            print(f"Your guess of {guess} is too low")
        else:
            print(f" Your guess of {guess} is just right!")
            break


# Loop breaks when the input ia just right

guessing_game()
