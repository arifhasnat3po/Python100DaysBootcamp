from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("C-3po")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="C-3po", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image)
unknown_button.config(bg=BACKGROUND_COLOR, highlightthickness=0)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
# check_image.config(bg=BACKGROUND_COLOR, highlightthickness=0)
known_button = Button(image=check_image)
# canvas.create_image(790, 300, image=check_image)
known_button.config(bg=BACKGROUND_COLOR, highlightthickness=0)
known_button.grid(row=1, column=1)

window.mainloop()
