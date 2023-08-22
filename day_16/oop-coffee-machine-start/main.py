from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

resource = Menu()
make_coffee = CoffeeMaker()
money = MoneyMachine()
is_on = True
while is_on:
    choice = input(f'What would you like? ({resource.get_items()}): ').lower()
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        make_coffee.report(), money.report()
    else:
        item = resource.find_drink(choice)
        if make_coffee.is_resource_sufficient(item):
            cost = item.cost
            if money.make_payment(cost):
                make_coffee.make_coffee(item)