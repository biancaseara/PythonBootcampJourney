import turtle as t
import random as r

colors = ['cornflower blue', 'green yellow', 'brown', 'purple', 'olive', 'orange red', 'crimson', 'navy', 'dodger blue']

sangie = t.Turtle()

repeat = 3
i = 0
while i < 11:
    sangie.color(r.choice(colors))

    for _ in range(repeat):
        sangie.forward(100)
        sangie.right(360/repeat)

    repeat += 1
    i += 1

screen = t.Screen()
screen.exitonclick()

