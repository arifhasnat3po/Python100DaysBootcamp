import turtle as t
import random
# from random import random
from turtle import Turtle, Screen
tim = Turtle()
tim.shape("turtle")

# colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "gray", "black", "white", "cyan", "magenta", "teal", "lavender", "maroon", "olive", "navy", "aquamarine", "turquoise", "silver", "lime", "gold", "violet", "indigo"]
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

move = ["forward", "left", "right"]
tim.speed('slow')
# tim.color(random.choice(colours))
tim.pensize(10)
for i in range(100):
    steps = int(random.random() * 100)
    angle = int(random.random() * 360)
    # tim.color(random.choice(colours))
    
    tim.right(angle)
    tim.fd(steps)
    tim.color(random.choice(colours))

t.screen.mainloop()

# tim.forward(1000)













# def draw_shape(num_sides):
#     angle = 360/num_sides

#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
        
        
# for shape_side_in in range(3,11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_in)
    



















screen = Screen()
screen.exitonclick()