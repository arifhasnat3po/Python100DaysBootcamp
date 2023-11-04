from tkinter import *

window = Tk()

window.title("Mile to Km converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


def button_clicked():
    input_value = float(input.get()) * 1.60934
    my_label_center.config(text=input_value)


my_label = Label(text="", font=("Arial", 24, "bold"))
my_label.grid(column=2, row=1)
my_label_left = Label(text="is equal to", font=("Arial", 24, "bold"))
my_label_left.grid(column=1, row=2)

my_label_right = Label(text="Miles", font=("Arial", 24, "bold"))
my_label_right.grid(column=3, row=1)


my_label_center = Label(text="0", font=("Arial", 24, "bold"))
my_label_center.grid(column=2, row=2)


my_label_center_right = Label(text="Km", font=("Arial", 24, "bold"))
my_label_center_right.grid(column=3, row=2)
# output_value = float(input_value) * 1.60934
button = Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=3)


input = Entry(width=10)
# input.pack()
input.get()
# input.pack()
input.grid(column=2, row=1)


window.mainloop()
