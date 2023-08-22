# Print the logo
from game_data import data
from art import logo, vs
import random
import os

def HigherLower():
    data_a = random.choice(data)
    score = 0
    game_over = False
    while not game_over:
        os.system('cls')
        print(logo)        
        data_b = random.choice(data)
        if data_a == data_b:
            data_b = random.choice(data)
        
        a_count = data_a['follower_count']
        b_count = data_b['follower_count']

        print(f"{data_a['name']}: {a_count}")
        print(f"{data_b['name']}: {b_count}")
       
        if score > 0:
            print(f"You're right! Current score: {score}.")

        print(f"Compare A: {data_a['name']}, a {data_a['description']}, from {data_a['country']}.")
        print(vs)
        print(f"Against B: {data_b['name']}, a {data_b['description']}, from {data_b['country']}.")

        user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

        if user_choice == 'A' and a_count > b_count:
            score += 1
            data_a = data_b
        elif user_choice == 'B' and b_count > a_count:
            score += 1
            data_a = data_b
        else:
            os.system('cls')
            print(logo)
            print(f"Sorry, that's wrong. Final Score: {score}")
            game_over = True

HigherLower()