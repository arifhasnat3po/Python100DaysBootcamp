from tkinter import *
import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(self.window, width=300,
                             height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.score_label = Label(text="Score:0",
                                 font=("Arial", 12),
                                 fg="white", bg=THEME_COLOR
                                 )
        self.score_label.grid(row=0, column=1)
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            text="Some Question Text", fill=THEME_COLOR, font=("Arial", 10, "italic"))
        # self.canvas.question_text.grid(row=1, column=0, columnspan=2, pady=50)
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image=false_image, highlightthickness=0, command=self.false_pressed)
        # self.false_button.config(padx=20, pady=20)
        self.false_button.grid(row=3, column=0)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(
            image=true_image, highlightthickness=0, command=self.true_pressed)
        # self.true_button.config(padx=20, pady=20)
        self.true_button.grid(row=3, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def true_pressed(self):
        # is_right =  self.quiz.check_answer("True")
        self.give_feedback(self.quiz.check_answer("True"))
        # self.canvas.delete(self.question_text)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        # self.canvas.delete(self.question_text)

    def give_feedback(self, is_right):
        # self.window.after(1000, func=)
        if is_right == True:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
