from art import logo
import random
import os

def game():
    os.system('cls')
    print(logo)
    print('Welcome to the Number Guessing Game!')
    number = random.randint(1, 100)
    # print(f"Pssst, the number is {number}")
    print("I'm thinking of a number between 1 and 100.")

    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        guesses = 10
    elif level == 'hard':
        guesses = 5

    game_over = False
    while not game_over:
        if guesses >= 1:
            print(f"You have {guesses} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if guess == number:
                print(f"You got it! The answer is {guess}.")
                game_over = True
            elif guess > number:
                print('Too high.')
                guesses -= 1    
            elif guess < number:
                print('Too low')
                guesses -= 1                
        else:
            print("You've run out of guesses, you lose.")
            game_over = True
    
    if game_over:
        if input('Start over? "yes" or "no": ').lower() == 'yes':
            game()
        else:
            return
game()