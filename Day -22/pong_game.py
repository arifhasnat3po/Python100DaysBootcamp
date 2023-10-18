from turtle import Turtle, Screen
from paddle import Paddle


screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))


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
    screen.update()




screen.exitonclick()





