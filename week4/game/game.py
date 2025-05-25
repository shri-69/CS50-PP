import random

def get_level():

    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
        except ValueError:
            pass
        print("Please enter a positive integer.")

def get_guess():

    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                return guess
        except ValueError:
            pass  # not an integer
        print("That wasn't a valid guess. Try a positive number.")
level = get_level()
secret_number = random.randint(1, level)
while True:
    guess = get_guess()

    if guess < secret_number:
        print("Too small!")
    elif guess > secret_number:
        print("Too large!")
    else:
        print("Just right!")
        break
