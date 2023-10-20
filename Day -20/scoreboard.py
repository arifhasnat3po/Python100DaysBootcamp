from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18 , "bold")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.updated_score()
        
        
        
        
    def updated_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align= ALIGNMENT, font= FONT)
        
    def increase_score(self):
        self.score +=1
        self.updated_score()
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.updated_score()
        
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align= ALIGNMENT, font= FONT)