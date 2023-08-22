import random
import os
from hangman_art import svt
from songs import songs

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print(svt)

chosen_song = random.choice(songs)
song_length = len(chosen_song)

print(svt)

# print(f'the chosen song is {chosen_song}.')
score = 6

display = []
for space in chosen_song:
    if space == " ":
        display.append(' ')
    else:
        display.append("_")
print(f'{" ".join(display)}')

end_of_game = False

print(f'Score: {score}')
while not end_of_game:
    guess = input('Enter a letter:\n').lower()
    clear()

    if guess in display:
        print(f'You already guessed {guess}.')

    for position in range(song_length):
        letter = chosen_song[position]
        
        if guess == letter:
            display[position] = letter

    if guess not in chosen_song:
        score -= 1
        print(f"{guess} is not in the song's name.")
        if score == 0:
            end_of_game = True
            print(f'You lose!\nThe song was {chosen_song}.')
    
    if '_' not in display:
        end_of_game = True
        print('You win!')

    print(f'Score: {score}\n{" ".join(display)}')