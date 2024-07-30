from art import logo, vs
from data import data
import random
import sys
import os


def clear():
    os.system('cls')


def question(data, int1, int2):
    print(f"Compare:\n\n"
          f"A: {data[int1]['name']}, a {data[int1]['description']}, from {data[int1]['country']}")
    print(vs)
    print(f"B: {data[int2]['name']}, a {data[int2]['description']}, from {data[int2]['country']}\n")
    user_guess = input("Who has more followers? Type 'A' or 'B': ")
    return user_guess


def check_results(user_guess, data, int1, int2, score):
    if user_guess.lower() == 'a':
        user_answer = int1
        other_answer = int2
    else:
        user_answer = int2
        other_answer = int1
    user_answer_followers = data[user_answer]['follower_count']
    other_answer_followers = data[other_answer]['follower_count']
    if user_answer_followers > other_answer_followers:
        score += 1
        print(f"Correct! Current score: {score}.")
        return score, user_answer
    else:
        print(f"Incorrect. You lose. Final score: {score}")
        sys.exit()


def main():
    print(logo)
    int1 = random.randint(1, 50)
    int2 = random.randint(1, 50)
    if int1 == int2:
        int2 = random.randint(1, 50)
    score = 0
    while True:
        user_guess = question(data, int1, int2)
        clear()
        print(logo)
        score, user_answer = check_results(user_guess, data, int1, int2, score)
        int1 = user_answer
        int2 = random.randint(1, 50)
        if int1 == int2:
            int2 = random.randint(1, 50)





main()
