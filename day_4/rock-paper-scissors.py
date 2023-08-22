import random
import sys

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

invalid = """
  ____________
 /            \
|   INVALID    |
|     INPUT    |
 \____________/
     /   \      
    /     \     
   /   ?   \    
  /    ___  \   
 |    /   \  |  
 |    \___/  |  
  \_________/  
"""
game_ascii = [rock, paper, scissors, invalid]

choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
if choice >= 0 and choice < len(game_ascii) - 1:
    print(game_ascii[choice])
else:
    print(game_ascii[3])
    print('You typed a invalid number. You lose!')
    sys.exit()

'''
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)
else:
    print(invalid)
'''

computer_choice = random.randint(0, 2)
print(f'Computer chose:\n{game_ascii[computer_choice]}')
'''
if computer_choice == 0:
    print(f'Computer chose:\n{rock}')
elif computer_choice == 1:
    print(f'Computer chose:\n{paper}')
else:
    print(f'Computer chose:\n{scissors}')
'''

if choice == computer_choice:
    print("It's a tie!")
elif choice == 0 and computer_choice == 2:
    print('You win!')
elif choice == 1 and computer_choice == 0:
    print('You win!')
elif choice == 2 and computer_choice == 1:
    print('You win!')
elif choice < 0 or choice > 2:
    print('You typed a invalid number. You lose!')
else:
    print('You lose!')

