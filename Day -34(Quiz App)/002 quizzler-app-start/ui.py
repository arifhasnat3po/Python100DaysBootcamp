from tkinter import *
import tkinter

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(self.window, width=300,
                             height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.score_label = Label(text="Score:0",
                                 font=("Arial", 12),
                                 fg="white", bg=THEME_COLOR
                                 )
        self.score_label.grid(row=0, column=1)
        self.question_text = self.canvas.create_text(
            150, 125, text="Some Question Text", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0)
        self.false_button.config(padx=20, pady=20)
        self.false_button.grid(row=3, column=0)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0)
        self.true_button.config(padx=20, pady=20)
        self.true_button.grid(row=3, column=1)

        self.window.mainloop()
