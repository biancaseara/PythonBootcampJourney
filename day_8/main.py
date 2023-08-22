'''
def greet():
    print('Hi!')
    print('How you doing?')
greet()
'''
# Functions with parameter(variable) and argument(value)
'''
def greet_w_name(name):
    print(f'Hi, {name}.\nHow you doing?')
greet_w_name('Bianca')
'''
# Functions with more than one parameter | positional argument
'''
def group(name, leader):
    print(f"{leader} is {name}'s leader.")

groups_name = input("What's the group's name: ")
leader_name = input("What's the leader's name: ")
# group('SVT', 'S.Coups')

group(groups_name, leader_name)
'''
# Functions with more than one parameter | keyword argument
def greet_with(name, location):
    print(f"Hi, {name}.")
    print(f"How is it like in {location}?")
greet_with(location='Jeju island', name='Seungkwan')
