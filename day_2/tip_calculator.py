print('Welcome to the tip calculator.')

# Asking the user the infos.
bill = float(input('What was the total bill? R$'))
tip = int(input('What percentage tip would like to give? 10, 12 or 15? '))
people_2_split = int(input('How many people to split the bill? '))

# Math operations.
bill_w_tip = bill * (1 + (tip / 100))
payment_p_person = round(bill_w_tip / people_2_split, 2)

print(f'Each person should pay: R${payment_p_person}')