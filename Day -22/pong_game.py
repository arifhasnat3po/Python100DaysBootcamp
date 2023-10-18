from turtle import Turtle, Screen
# from paddle import Paddle





screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")


paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid = 5, stretch_len = 1)
paddle.penup()
paddle.goto(-350, 0)


def go_up():
    y = paddle.ycor()
    y += 20
    paddle.sety(y)
    
def go_down():
    y = paddle.ycor()
    y -= 20
    paddle.sety(y)

screen.listen()
screen.onkey(go_up,"Up")
screen.onkey(go_down,"Down")
def stop_movement():
    screen.onkeypress(go_up, "Up")  # Remove the binding for the "Up" key
    screen.onkeypress(go_down, "Down")  # Remove the binding for the "Down" key

# Bind the "Up" and "Down" keys to stop movement when released
screen.onkey(stop_movement, "Up")
screen.onkey(stop_movement, "Down")
# paddle.move()











screen.exitonclick()





