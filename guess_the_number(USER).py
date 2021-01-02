# @Author : Samuel Anumudu
# Project: Guess the number (USER)

# About : This is a guessing game where the user has a secret number and we are trying to guess that secret number


# Let the user generate a number for us to guess

import random


def computer_guess(n):
    low = 1
    high = n
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # Could also be high because low = high
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)")
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print(f'Yah! The computer guessed your number, {guess}, correctly!')


computer_guess(100)