import turtle as t
import random
# from random import random
from turtle import Turtle, Screen
tim = Turtle()
tim.shape("turtle")

# colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "gray", "black", "white", "cyan", "magenta", "teal", "lavender", "maroon", "olive", "navy", "aquamarine", "turquoise", "silver", "lime", "gold", "violet", "indigo"]
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

move = [0,90,180,270]
tim.speed('fastest')
t.colormode(255)

def random_color() :
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color
    



tim.pensize(15)
for i in range(200):
    # steps = int(random.random() * 100)
    # angle = int(random.random() * 360)
    # tim.color(random.choice(colours))
    tim.setheading(random.choice(move))
    
    # tim.right(angle)
    # tim.fd(steps)
    tim.forward(30)
    tim.color(random_color())

t.screen.mainloop()















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