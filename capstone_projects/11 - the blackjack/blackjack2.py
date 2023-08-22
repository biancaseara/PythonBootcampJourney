import random
from art import logo
import os
import platform

def clear():
    # if os.name == 'nt':
    if platform.system() == 'Windows':
        os.system('clear')
        os.system('cls')
    else:
        os.system('clear')

def deal_card():
    """Returns a random item from the list"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    '''Take a list of cards and return the score calculated from the cards'''
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return 'You went over. You lose!'
    
    if computer_score == user_score:
        return "Draw!"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack!"
    elif user_score == 0:
        return "Win with a Blackjack!"
    elif user_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Opponent went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

def blackjack_game():
    print(logo)
    user_cards = []
    computer_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or user_score > 21 or computer_score == 0:
            game_over = True
        else:
            deal_again = input("Type 'y' to get another card, type 'n' to pass: ")
            if deal_again == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"You final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score=user_score, computer_score=computer_score))

    end_of_game = False
    while not end_of_game:
        if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
            clear()
            blackjack_game()
        else:
            end_of_game = True
            break

blackjack_game()