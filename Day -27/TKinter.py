# import tkinter
from tkinter import *


def button_clicked():
    print("Button clicked!")
    # my_label.config(text="Button clicked")
    my_label.config(text=input.get())


window = Tk()

window.title("My first GUE program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


# Label
my_label = Label(text="You are a Human", font=("Arial", 24, "bold"))

# my_label.pack()
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
# my_label.config(text=button_clicked)

# button
new_button = Button(text="Click Me", command=button_clicked)

# button.pack()
# # in order to show on the screen
new_button.grid(column=2, row=0)

button = Button(text="Click Me", command=button_clicked)

# button.pack()
# # in order to show on the screen
button.grid(column=1, row=1)

# Entry
input = Entry(width=10)
# input.pack()
input.get()
# input.pack()
input.grid(column=3, row=2)


window.mainloop()
