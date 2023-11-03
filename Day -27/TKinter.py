# import tkinter
from tkinter import *
window = Tk()

window.title("My first GUE program")
window.minsize(width=500, height=300)


# Label
my_label = Label(text="You are a Human", font=("Arial", 24, "bold"))


my_label.pack()
# my_label.config(text=button_clicked)

# button


def button_clicked():
    print("Button clicked!")
    # my_label.config(text="Button clicked")
    my_label.config(text=input.get())


button = Button(text="Click Me", command=button_clicked)

button.pack()  # in order to show on the screen


# Entry
input = Entry(width=10)
input.pack()
input.get()


window.mainloop()
