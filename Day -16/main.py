# # import turtle
# # timmy = turtle.Turtle()

# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkGreen", "DarkGreen")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

import prettytable
from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"]) 
table.add_column("Type",["Electric","Water","Fire"])
print(table)


# from prettytable import from_csv fp = open("mytable.csv", "r") pt = from_csv(fp) fp.close()