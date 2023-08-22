from turtle import Turtle
import random

SIZE = 0.8

colors = [
    'dodgerblue', 'steelblue', 'mediumblue', 'darkblue', 'mediumslateblue',
    'blueviolet', 'darkviolet', 'mediumorchid', 'darkorchid', 'violet',
    'hotpink', 'deeppink', 'mediumvioletred', 'palevioletred', 'mediumspringgreen',
    'limegreen', 'forestgreen', 'darkolivegreen', 'goldenrod', 'darkorange',
    'orange', 'coral', 'tomato', 'orangered', 'gold', 'yellow', 'lightyellow'
]


class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=SIZE, stretch_wid=SIZE)
        self.color('blue')
        self.speed('fastest')
        self.refresh()
    
    def refresh(self):
        random_x = random.randint(-260, 280)
        random_y = random.randint(-280, 280)
        self.goto(x=random_x, y=random_y)
        self.color(random.choice(colors))
        