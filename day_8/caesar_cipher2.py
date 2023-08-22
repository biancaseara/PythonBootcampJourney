from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alpha_len = len(alphabet)

def caesar(direction, text, shift):
    plain_text = ''
    for letter in text:
        if letter not in alphabet:
            plain_text += letter
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction == 'encode':
                position = (position + shift) % alpha_len
                plain_text += alphabet[position]
            elif direction == 'decode':
                position = (position - shift) % alpha_len
                plain_text += alphabet[position]
    print(f'The {direction}d text is {plain_text}')

print(logo)

should_continue = True
while should_continue:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(direction=direction, text=text, shift=shift)

        try_again = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
        if try_again == 'no':
             should_continue = False