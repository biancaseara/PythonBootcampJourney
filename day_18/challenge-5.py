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


sangie.speed(0)


def draw_spirograph(size_of_gap):
    for _ in range(360 // size_of_gap):
        sangie.color(random_color())
        sangie.circle(100)
        sangie.setheading(sangie.heading() + size_of_gap)


draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()
