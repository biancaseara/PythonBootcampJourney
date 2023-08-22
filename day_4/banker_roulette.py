import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

num_of_people = len(names)

# "It's (-1) because the number of people is greater than the number in the list, and since the list starts counting from zero, we need to subtract one to get the correct index."
random_number = random.randint(0, num_of_people - 1)

who_pays = names[random_number]

print(f'{who_pays} is going to buy the meal today!')