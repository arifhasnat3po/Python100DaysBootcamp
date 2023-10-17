from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# starting_position = [(0,0), (-20,0), (-40,0)]

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
    
# screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    
#Detect collision with food
    if snake.head.distance(food) < 18:
        # print("nom nom nom") 
        food.refresh()
        score.updated_score()
        score.increase_score()
    
    







screen.exitonclick()