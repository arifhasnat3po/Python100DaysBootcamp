from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.updated_score()
        
        
        
        
    def updated_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 18 , "bold"))
        
    def increase_score(self):
        self.score +=1
        self.updated_score()