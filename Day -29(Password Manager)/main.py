from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")

canvas = Canvas(width=200, height=200)
mypass_img = PhotoImage(
    file="C:/Users/ahpar/Documents/100daysofPython/Day -29(Password Manager)/logo.png")  # Use forward slashes
window.config(padx=100, pady=50, highlightthickness=0)
canvas.create_image(100, 100, image=mypass_img)
canvas.grid(column=2, row=2)

window.mainloop()
