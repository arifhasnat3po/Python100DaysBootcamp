import turtle as t
import random
from turtle import Turtle, Screen
tim = Turtle()
tim.shape("turtle")

colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "gray", "black", "white", "cyan", "magenta", "teal", "lavender", "maroon", "olive", "navy", "aquamarine", "turquoise", "silver", "lime", "gold", "violet", "indigo"]

def draw_shape(num_sides):
    angle = 360/num_sides

    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)
        
        
for shape_side_in in range(3,11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_in)
    



















screen = Screen()
screen.exitonclick()