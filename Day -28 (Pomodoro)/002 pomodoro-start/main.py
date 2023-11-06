from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

timer = NONE
reps = 0
# ---------------------------- TIMER RESET ------------------------------- #


def reset_clicked():
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN, font=(
        FONT_NAME, 34, "bold"), bg=YELLOW, highlightthickness=0)
    canvas.itemconfig(timer_text, text="00:00")

    check_label.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_clicked():
    global reps

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60

    reps += 1

    if reps == 8:
        count_down(long_break_min)
        timer_label.config(text="Break", fg=RED)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break", fg=PINK)
    # count_down(5 * 60)
    # count_down(15)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"

    elif count_sec <= 9:
        count_sec = f"{0}{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_clicked()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"

        check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO")


canvas = Canvas(width=200, height=224, bg=YELLOW)
tomato_img = PhotoImage(
    file="C:\\Users\\ahpar\\Documents\\100daysofPython\\Day -28 (Pomodoro)\\002 pomodoro-start\\tomato.png")
window.config(padx=100, pady=50, bg=YELLOW, highlightthickness=0)
canvas.create_image(102, 112, image=tomato_img)

timer_text = canvas.create_text(103, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))


# canvas.pack()
canvas.grid(column=2, row=2)


timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 34, "bold"))
timer_label.config(bg=YELLOW, highlightthickness=0)
timer_label.grid(column=2, row=1)

check_label = Label(fg=GREEN, font=(FONT_NAME, 18, "bold"))
check_label.config(bg=YELLOW, highlightthickness=0)
check_label.grid(column=2, row=4)


start_button = Button(text="Start", command=start_clicked)
start_button.grid(column=1, row=3)


reset_button = Button(text="Reset", command=reset_clicked)
reset_button.grid(column=3, row=3)

window.mainloop()
