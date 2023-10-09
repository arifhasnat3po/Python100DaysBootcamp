import turtle as t
import random

from turtle import Turtle, Screen
tim = Turtle()
tim.shape("turtle")

tim.speed('fastest')
t.colormode(255)

def random_color() :
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color
    
    
for i in range(200):
    # steps = int(random.random() * 100)
    # angle = int(random.random() * 360)
    angle = 5
    tim.circle(100)
    tim.left(angle)
    
    # tim.right(angle)
    # tim.fd(steps)
    # tim.forward(30)
    tim.color(random_color())
















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