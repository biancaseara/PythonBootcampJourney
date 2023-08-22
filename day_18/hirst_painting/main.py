import turtle as t
from random import choice

color_list = [
    (198, 13, 32), (250, 237, 19), (39, 76, 189), (39, 217, 68), (238, 227, 5), (229, 159, 47), (28, 40, 156), (214, 75, 13), (16, 154, 16), (198, 15, 11), (243, 34, 165), (68, 10, 30), (228, 18, 120), (60, 15, 8), (223, 141, 209), 
    (11, 97, 62), (221, 161, 9), (50, 212, 231), (18, 20, 47), (11, 227, 239), (238, 156, 217), (84, 74, 211), (78, 210, 163), (82, 234, 200), (61, 233, 241), (5, 68, 42), (216, 90, 52), (173, 178, 231), (235, 170, 164), (8, 244, 224), (248, 9, 44)
]

screen = t.Screen()
screen.setup(0.7, 0.9)

painting = t.Turtle()
painting.speed('fastest')
t.colormode(255)
painting.up()
painting.hideturtle()

y = -200.00
while y <= 250:
    painting.goto(-250.00, y)

    for _ in range(10):
        painting.dot(20, choice(color_list))
        painting.penup()
        painting.forward(50)

    y += 50

screen.exitonclick()
