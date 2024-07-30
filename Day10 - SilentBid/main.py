import os
from art import logo


# HINT: You can call clear() to clear the output in the console.

def clear():
    os.system('cls')
from art import logo

def ask_user():
  while True:
      name = input(str("What's your name? "))
      bid = input("What is your max bid? ")
      bidding_dict = dict()
      bidding_dict[name] = bid
      response = input("Is there another person who would like to bid? Type y or n. ")
      if response.lower() != 'y':
          clear()
          return bidding_dict
      else:
          clear()
          continue


def check_bid(bidding_dict):
  for bid in bidding_dict:
      winning_bid = 0
      value = int(bidding_dict[bid])
      if value > winning_bid:
          result_name = bid
          result_bid = value
          return result_name, result_bid
      else:
          continue


def main():
  print(logo)
  print("Welcome to the silent auction bid.")
  bidding_dict = ask_user()
  result_name, result_bid = check_bid(bidding_dict)
  print(f"{result_name} has won the auction with a bid of {result_bid}.")


main()