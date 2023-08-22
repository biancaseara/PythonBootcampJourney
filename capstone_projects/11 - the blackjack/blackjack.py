import random
from art import logo
import os
import platform

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
        os.system('clear')
    else:
        os.system('clear')

def deal_card():
    clear()
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_choice = random.choices(cards, k=2)
    computer_choice = random.choices(cards, k=2)
    def check(score_user, score_computer, user_choice, computer_choice):
        if score_user > 21 or score_computer > 21:
            cards[0] = 1
            if score_user > 21:
                print(f"Your final hand: {user_choice}, final score: {score_user}\nComputer's final hand: {computer_choice}, final score: {score_computer}")
                print('You went over. You lose!')
            elif score_computer > 21:
                print(f"Your final hand: {user_choice}, final score: {score_user}\nComputer's final hand: {computer_choice}, final score: {score_computer}")
                print('Opponent went over. You win!')
            return
        elif score_user > score_computer and score_user <= 21:
            print(f"Your final hand: {user_choice}, final score: {score_user}\nComputer's final hand: {computer_choice}, final score: {score_computer}")
            print('You win!')
            return 
        elif score_computer > score_user and score_computer <= 21:
            print(f"Your final hand: {user_choice}, final score: {score_user}\nComputer's final hand: {computer_choice}, final score: {score_computer}")
            print('You lose!')
            return
        else:
            return
    
    if 11 in user_choice and 10 in user_choice and 11 in computer_choice and 10 in computer_choice:
        print("Computer got a blackjack. You lose!")
        print(f'user: {user_choice}\ncomputer: {computer_choice}')
        return deal_card()
    elif 11 in computer_choice and 10 in computer_choice:
        print("Computer got a blackjack. You lose!")
        print(f'user: {user_choice}\ncomputer: {computer_choice}')
        return deal_card()      
    elif 11 in user_choice and 10 in user_choice:
        print('You got a blackjack. You win!')
        print(f'user: {user_choice}\ncomputer: {computer_choice}')
        return deal_card()
    else:
        computer_card = random.sample(computer_choice, k=1)
        game_over = False
        while not game_over:
            score_user = sum(user_choice)
            score_computer = sum(computer_choice)
            print(f"Your cards: {user_choice}, current score: {score_user}\nComputer's first card: {computer_card}")

            another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if another_card == 'y':            
                user_choice.append(random.choice(cards))
                score_user = sum(user_choice)
                if score_user >= 21:
                    check(score_user=score_user, score_computer=score_computer, user_choice=user_choice, computer_choice=computer_choice)
                    game_over = True
            elif another_card == 'n':
                while score_computer <= 16:
                    computer_choice.append(random.choice(cards))
                    score_computer = sum(computer_choice)

                check(score_user=score_user, score_computer=score_computer, user_choice=user_choice, computer_choice=computer_choice)
                game_over = True
            else:
                return 'You did not type a valid option.'              
    
    if input('Do you want to play a game of Blackjack? Type "y" or "n": ') == 'y':
        deal_card()
deal_card()