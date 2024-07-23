from art import logo
import os
import random
import sys


def clear():
    os.system('cls')


def make_dealers_hand(cards):
    dealers_hand = []
    for card in range(2):
        card = random.choice(cards)
        dealers_hand.append(card)
    return dealers_hand


def make_hand(cards):
    hand = []
    for card in range(2):
        card = random.choice(cards)
        hand.append(card)
    return hand


def check_for_blackjack(dealers_hand, hand):
    if [11, 10] in dealers_hand:
        sys.exit("Blackjack. My win. Thanks for the soul, sucker.")
    elif [11, 10] in hand:
        sys.exit("Blackjack. I guess you win this time.")
    else:
        pass


def check_eleven(cards):
    if 11 in cards:
        total = sum(cards)
        if total > 21:
            for i in range(len(cards)):
                if cards[i] == 11:
                    cards[i] = 1
            return cards
        else:
            return cards
    else:
        return cards


def deal(hand, dealers_hand):
    total = sum(hand)
    want_card = input(f"\nYour cards are {hand}. The total of your hand is {total}.\n"
                      f"The dealer's open card is {dealers_hand[0]}.\n"
                      f"Would you like another card? Type 'y' or 'n': ")
    return want_card


def hit_me(hand, cards):
    card3 = random.choice(cards)
    hand.append(card3)
    total = sum(hand)
    if total > 21:
        hand = check_eleven(hand)
        total = sum(hand)
        if total > 21:
            print(f"\nYour cards are {hand}. The total of your hand is {total}.\nBust! You're over 21. Thanks for the "
                  f"soul, sucka.")
            sys.exit()
        else:
            print(f"\nYour cards are {hand}. The total of your hand is {total}.")
            return total, hand
    else:
        print(f"\nYour cards are {hand}. The total of your hand is {total}.")
        return total, hand


def dealers_draw(dealers_hand, cards):
    dealers_total = sum(dealers_hand)
    while dealers_total <= 16:
        card3 = random.choice(cards)
        dealers_hand.append(card3)
        dealers_total = sum(dealers_hand)
    if dealers_total > 21:
        dealers_hand = check_eleven(dealers_hand)
        dealers_total = sum(dealers_hand)
        if dealers_total > 21:
            print("The dealer went bust. You got lucky this time.")
            sys.exit()
        else:
            return dealers_hand
    else:
        return dealers_hand


def check_results(hand, dealers_hand):
    total = sum(hand)
    dealer_total = sum(dealers_hand)
    print(f"\nYour final hand is {hand} for a total of {total}.\nThe dealer's final hand is {dealers_hand} for a "
          f"total of {dealer_total}.")
    if total > dealer_total:
        print("You win this round. I'll be back again.")
    elif dealer_total > total:
        print("Thanks for the soul, sucker. Better luck next time!")
    if total == dealer_total:
        print("Guess you kept to keep your soul this time. Whaddya say to another round?")


def main():
    print(logo)
    intro = ("Let's play a game of Blackjack. Winner gets to keep the other's soul? What do ya say?\nType 'y' for yes "
             "or 'n' for no: ")
    start = ""
    while start.lower() != "y":
        start = input(intro)
    print("\nYou thought you had a choice? Hah! Let's start the game!")
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    dealers_hand = make_dealers_hand(cards)
    hand = make_hand(cards)
    check_for_blackjack(dealers_hand, hand)
    hand = check_eleven(hand)
    dealers_hand = check_eleven(dealers_hand)
    want_card = deal(hand, dealers_hand)
    while want_card.lower() == "y":
        total, hand = hit_me(hand, cards)
        if total > 21:
            print("Bust! You lose. Thanks for your soul.")
            sys.exit()
        else:
            want_card = input("Would you like another card? Type 'y' or 'n': ")
    dealers_hand = dealers_draw(dealers_hand, cards)
    check_results(hand, dealers_hand)
    again = input("Care to try your luck again?")
    if again.lower() == "y":
        clear()
        main()
    else:
        sys.exit()


main()
