from tkinter import *
import pandas as pd
import random
import time

BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv(
    r"C:\Users\ahpar\Documents\100daysofPython\Day -31 (Flashy Language App)\data\german_words.csv")
print(data)
df = data.to_dict(orient="records")
# print(df)
# word = df[random.randint(0, len(df)-1)]["German"]
# print(word)

current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(df)
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=current_card["German"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global current_card, flip_timer
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)
    # flip_timer = window.after(3000, func=next_card)


window = Tk()
window.title("C-3po")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(
    400, 150, text="C-3po", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(
    400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, command=next_card)
unknown_button.config(bg=BACKGROUND_COLOR, highlightthickness=0)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
# check_image.config(bg=BACKGROUND_COLOR, highlightthickness=0)
known_button = Button(image=check_image, command=next_card)
# canvas.create_image(790, 300, image=check_image)
known_button.config(bg=BACKGROUND_COLOR, highlightthickness=0)
known_button.grid(row=1, column=1)

next_card()
window.mainloop()
