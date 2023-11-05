from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO")


canvas = Canvas(width=200, height=224, bg=YELLOW)
tomato_img = PhotoImage(
    file="C:\\Users\\ahpar\\Documents\\100daysofPython\\Day -28 (Pomodoro)\\002 pomodoro-start\\tomato.png")
window.config(padx=100, pady=50, bg=YELLOW, highlightthickness=0)
canvas.create_image(102, 112, image=tomato_img)

canvas.create_text(103, 130, text="00:00", fill="white",
                   font=(FONT_NAME, 35, "bold"))

canvas.pack()


window.mainloop()
