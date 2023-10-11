from turtle import Turtle, Screen

tim = Turtle()

screen = Screen()

def move_forwards():
    tim.forward(20)

def move_backwards():
    tim.backward(20)

def move_circle():
    new_heading = tim.heading() + 20
    tim.setheading(new_heading)
   
  
    
def anti_circle():
    new_heading = tim.heading() - 20
    tim.setheading(new_heading)
 
# screen.onkey(move_forwards,'w') # w is the key for moving forward and onkey takes in a function name as
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key = "w", fun = move_forwards)
screen.onkey(key = "s", fun = move_backwards)
screen.onkey(key = "d", fun = move_circle)
screen.onkey(key = "a", fun = anti_circle)
screen.onkey(key = "c", fun = clear)
# clear()

screen.exitonclick()
