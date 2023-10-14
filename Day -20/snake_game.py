from turtle import Screen, Turtle

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")


snake1 = Turtle()
snake1.shape("square")
snake1.color("white")
snake1.goto(-20,0)

snake2 = Turtle()
snake2.shape("square")
snake2.color("white")
snake2.goto(0,0)

snake3 = Turtle()
snake3.shape("square")
snake3.color("white")
snake3.goto(20,0)










screen.exitonclick()