from tkinter import *
import tkinter

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.canvas = Canvas(width=200, height=224, bg=THEME_COLOR)
        self.window.mainloop()
