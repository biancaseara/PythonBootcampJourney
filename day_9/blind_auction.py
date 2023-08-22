from clear_func import clear
from art import logo

print(logo)

bidders = {}

def add_bidder(name, price):
    bidders[name] = price

still_bidders = True
while still_bidders:
    name_bidder = input('What is your name? ')
    bid_price = float(input('What is our bid? $'))
    other_bidder = input('Are there any other bidders? Type "yes" or "no". ').lower()
    add_bidder(name=name_bidder, price=bid_price)
    clear()

    if other_bidder == 'no':
        still_bidders = False

highest_bid = 0
for bidder in bidders:
    bid = bidders[bidder]
    if bid > highest_bid:
        highest_bid = bid
        winner = bidder

print(f'The winner is {winner} with a bid of {highest_bid}')