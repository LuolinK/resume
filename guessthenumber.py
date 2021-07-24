"""

*** GUESS THE NUMBER - GAME ***

This is a small script, which simulates
a number guessing game.

@author: Kevin
@date: 2021-07-08

"""

#
# * * * [Imports] * * *
#

import random


#
# * * * [Functions] * * *
#

def print_logo():
    print("Welcome to Number guessing name!")

    logo = """
      / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
     / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
    / /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
    \____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
    """

    print(logo)


def choose_difficulty():
    difficulty = input("Choose a difficulty, type 'easy' or 'hard': ")
    if difficulty == "easy":
        lifes = 10
        # print(f"You have {life} attempts to guess the number.")

    elif difficulty == "hard":
        lifes = 5
        # print(f"You have {life} attempts to guess the number.")
    else:
        print("Please choose a vaild difficulty level.")
        lifes = 0

    return lifes


def generate_random_number():
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    return answer


def make_the_guess(lifes, answer):
    while True:

        print(f"You have {lifes} attempts to guess the number.")
        guess = int(input("Make a guess: "))

        if guess == answer:
            result = "You win."
            print("Congrats! You won!")
            # Here you wanna stop!
        elif guess < answer:
            lifes -= 1
            result = "Too low."
        else:
            lifes -= 1
            result = "Too high."
        # return result
        print(result)

        if result == "You win." or lifes == 0:
            break


#
# * * * [Main Function] * * *
#

def play_the_game():
    # Step 1: Print The Logo to the User
    print_logo()

    # Step 2: Choose the Games difficulty
    lifes = choose_difficulty()

    # Step 3: Get a random number
    answer = generate_random_number()

    # Step 4: Make your guess
    make_the_guess(lifes, answer)

play_the_game()
