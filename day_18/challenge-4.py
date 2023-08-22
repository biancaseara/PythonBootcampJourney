import turtle as t
import random

sangie = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    r_color = (r, g, b)
    return r_color


orientations = [0, 90, 180, 270]
sangie.speed('fastest')
sangie.pensize(10)

screen = t.Screen()

for _ in range(500):
    sangie.color(random_color())
    sangie.setheading(random.choice(orientations))
    sangie.forward(20)

screen.exitonclick()
