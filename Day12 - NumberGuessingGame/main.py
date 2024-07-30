from art import logo
import random
import sys


def set_difficulty():
    difficulty = input("Choose your difficulty -- easy or hard: ")
    if difficulty.lower() == "easy":
        attempts = 10
        return attempts
    elif difficulty.lower() == "hard":
        attempts = 5
        return attempts
    else:
        raise ValueError("Incorrect response. Try again.")


def set_number():
    number = random.randint(1, 100)
    return number


def guess(attempts, number):
    while attempts > 1:
        user_guess = int(input("Guess a number: "))
        if user_guess > number:
            attempts -= 1
            print(f"Too high~ You have {attempts} chances left.")
        elif user_guess < number:
            attempts -= 1
            print(f"Too low~ You have {attempts} chances left.")
        elif user_guess == number:
            print("You guessed right. You win!")
            sys.exit()
    print("WRONG! You used up all your chances. You lose.")


def main():
    print(logo)
    print("Welcome to the Number Guessing Game.\nI'm thinking of a number between 1 and 100.\nCan you guess it?")
    attempts = set_difficulty()
    number = set_number()
    print(f"You have {attempts} chances to guess the number.")
    guess(attempts, number)


main()
