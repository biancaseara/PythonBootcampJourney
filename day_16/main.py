# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape('turtle')
# timmy.color('DarkGreen')
# timmy.forward(100)
# timmy.back(300)
# timmy.fillcolor('green')
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
tasks = ['Speaking', 'Writing', 'Reading', 'Listening']
due_date = ['23.04', '24.04', '25.04', '26.04']
table.add_column('Task', tasks)
table.add_column('Due Date', due_date)
table.align = 'l'
table.header_style = 'upper'
table.title = 'TODO LIST'
print(table)