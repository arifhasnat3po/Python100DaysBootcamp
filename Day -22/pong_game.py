from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time



screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

ball = Ball()
scoreboard = Scoreboard()


screen.listen()

def stop_movement():
    screen.onkeypress(l_paddle.go_up, "w")  # Remove the binding for the "Up" key
    screen.onkeypress(l_paddle.go_down, "s")  # Remove the binding for the "Down" key
    screen.onkeypress(r_paddle.go_up, "Up")  # Remove the binding for the "Up" key
    screen.onkeypress(r_paddle.go_down, "Down")  # Remove the binding for the "Down" key

# Bind the "Up" and "Down" keys to stop movement when released
screen.onkey(stop_movement, "w")
screen.onkey(stop_movement, "s")
screen.onkey(stop_movement, "Up")
screen.onkey(stop_movement, "Down")
# paddle.move()






game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()


    #Detecting collision with wall
    
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()
    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()
        
    # Detect if the ball goes out of bounds on the right side
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect if the ball goes out of bounds on the left side
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()





