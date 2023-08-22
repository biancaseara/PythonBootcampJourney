alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    encoded_text = ''
    for letter in plain_text:
        if letter in alphabet:        
            alpha_index = alphabet.index(letter)
            alpha_index = (alpha_index + shift_amount) % len(alphabet)
            encoded_text += alphabet[alpha_index]       
        else:
            encoded_text += letter
    print(f'The encoded text is {encoded_text}')

def decrypt(plain_text, shift_amount):
    decoded_text = ''
    for letter in plain_text:
        if letter in alphabet:
            alpha_index = alphabet.index(letter)
            alpha_index = (alpha_index - shift_amount) %len(alphabet)
            decoded_text += alphabet[alpha_index]
        else:
            decoded_text += letter
    print(f'The decoded text is {decoded_text}')

if direction == 'encode':
    encrypt(plain_text=text, shift_amount=shift)
elif direction == 'decode':
    decrypt(plain_text=text, shift_amount=shift)