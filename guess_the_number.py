# @Author : Samuel Anumudu
# Project: Guess the number (Computer)

# About : This is a guessing game where the computer has a secret number and we are trying to guess that secret number

# Let the computer generate a number for us to guess

import random


def guess(n):
    random_number = random.randint(1, n)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {n}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low")
        elif guess > random_number:
            print("Sorry, guess again. Too high!")

    print(f'Great! Congrats. You have guessed the number {random_number} correctly!')


guess(10)


