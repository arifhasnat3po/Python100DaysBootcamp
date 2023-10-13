from turtle import Turtle, Screen

screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "green","yellow", "blue", "purple"]

y_positions = [-100,-60,-20, 20, 60, 100]

for i in range(0, 6):   

    tim = Turtle(shape = "turtle")
    tim.color(colors[0])
    tim.penup()

    tim.goto(x=-230, y=y_positions[i])


tom = Turtle(shape = "turtle")
tom.color(colors[1])
tom.penup()

tom.goto(x=-230, y=-60)



dom = Turtle(shape = "turtle")
dom.color(colors[2])
dom.penup()

dom.goto(x=-230, y=-20)


com = Turtle(shape = "turtle")
com.color(colors[3])
com.penup()

com.goto(x=-230, y=20)


bom = Turtle(shape = "turtle")
bom.color(colors[4])
bom.penup()

bom.goto(x=-230, y=60)

aom = Turtle(shape = "turtle")
aom.color(colors[5])
aom.penup()

aom.goto(x=-230, y=100)


screen.exitonclick()