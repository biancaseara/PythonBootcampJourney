MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    '''Returns a resources report'''
    global money
    for resource in resources:
        if resource == 'water':
            print(f'Water: {resources[resource]}ml')
        if resource == 'milk':
            print(f'Milk: {resources[resource]}ml')
        if resource == 'coffee':
            print(f'Coffee: {resources[resource]}g')
    print(f'Money: ${money}')


def check_resources():
    '''Returns True when order can be made, False if ingredients are insufficient'''
    drink = MENU.get(choice)
    if drink:
        if drink['ingredients']['water'] > resources['water']:
            print('Sorry, there is not enough water')
            return False
        if drink['ingredients']['coffee'] > resources['coffee']:
            print('Sorry, there is not enough coffee')
            return False
        if 'milk' in drink['ingredients'] and drink['ingredients']['milk'] > resources['milk']:
            print('Sorry, there is not enough milk')
            return False
        return True
    else:
        print('Sorry, that drink is not available')
        return False


def process_coins():
    '''Process the coins, and return True when the payment is accepted, or False if money is insufficient'''
    global money
    if check_resources():
        print('Please insert coins.')
        quarter = int(input('how many quarters?: ')) * 0.25
        dime = int(input('how many dimes?: ')) * 0.10
        nickel = int(input('how many nickels?: ')) * 0.05
        penny = int(input('how many pennies?: ')) * 0.01

        sum_coins = quarter + dime + nickel + penny
        drink_cost = MENU.get(choice)
        drink_cost = drink_cost['cost']

        if sum_coins >= drink_cost:
            if sum_coins > drink_cost:
                change = sum_coins - drink_cost
                print(f'Here is ${round(change, 2)} in change')
            money += drink_cost
            return True
        elif sum_coins < drink_cost:
            print("Sorry, that's not enough money. Money refunded.")
            return False


def make_coffee():
    '''Deduct the required ingredients from the resources'''
    if process_coins():
        ingredients = MENU.get(choice)
        ingredients = ingredients['ingredients']
        for value in ingredients:
            for item in resources:
                if value == item:
                    resources[item] -= ingredients[value]
        print(f'Here is your {choice} ☕. Enjoy!')


is_on = True
while is_on:
    choice = input('What would you like? (espresso/latte/cappuccino): ').lower()
    if choice == 'report':
        report()
    elif choice == 'off':
        is_on = False
    else:
        if not check_resources():
            is_on = False
        else:
            make_coffee()