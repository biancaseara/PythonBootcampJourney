from turtle import Screen, Turtle
import random

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []

is_race_on = False

screen = Screen()
screen.setup(width=700, height=600)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')

y = -80
pos = 0
for new_turtle in colors:
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[pos])
    new_turtle.penup()
    new_turtle.goto(x=-335, y=y)
    all_turtles.append(new_turtle)
    y += 30
    pos += 1

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 325:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f'You\'ve won! The {winning_color} turtle is the winner!')
            else:
                print(f'You\'ve lost! The {winning_color} turtle is the winner!')

        rand_distance = random.randint(0, 15)
        turtle.forward(rand_distance)
    
screen.exitonclick()
