import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

chosen_letter = []
for letter in range(0, nr_letters):
    random_letter = random.choice(letters)
    chosen_letter.append(random_letter)
result_letter = ''.join(chosen_letter)

chosen_number = []
for number in range(0, nr_numbers):
    random_number = random.choice(numbers)
    chosen_number.append(random_number)
result_number = ''.join(chosen_number)

chosen_symbol = []
for symbol in range(0, nr_symbols):
    random_symbol = random.choice(symbols)
    chosen_symbol.append(random_symbol)
result_symbol = ''.join(chosen_symbol)

password = result_letter + result_number + result_symbol
shuffled_password = list(password)
random.shuffle(shuffled_password)
result_password = ''.join(shuffled_password)

print(result_password)