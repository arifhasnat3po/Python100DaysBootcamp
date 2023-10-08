from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("sea green")
for _ in range(15):
    tim.forward(10)
    tim.penup()
    # tim.color("white")
    tim.forward(10)
    tim.pendown()
    # tim.color("black")

# import heroes
# print(heroes.gen())
tim









screen = Screen()
screen.exitonclick()