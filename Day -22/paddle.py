from turtle import Turtle

# POSITION = ()
# STARTING_POSITIONS = [(0,20), (0,0), (0,-20)]
# MOVE_DISTANCE = 20
# UP = 90
# DOWN = 270

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("White")
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.penup()
        self.goto(position)


    def go_up(self):
        y = self.ycor()
        y += 20
        self.sety(y)
        
    def go_down(self):
        y = self.ycor()
        y -= 20
        self.sety(y)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

#     def up(self):
#         if self.head.heading() !=DOWN:
#             self.head.setheading(UP)
            
#     def down(self):
#         if self.head.heading() != UP:
#             self.head.setheading(DOWN)