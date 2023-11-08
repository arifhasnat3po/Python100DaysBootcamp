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
canvas.grid(column=1, row=1)

website_label = Label(text="Website:")
website_label.grid(column=0, row=3)

website_input = Entry(width=35)
website_input.get()
website_input.grid(column=1, columnspan=2, row=3)


email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=4)

email_input = Entry(width=35)
email_input.get()
email_input.grid(column=1, columnspan=2, row=4)


password_label = Label(text="Password:")
password_label.grid(column=0, row=5)

password_input = Entry(width=35)
password_input.get()
password_input.grid(column=1, columnspan=2, row=5)


generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=5)

add_button = Button(text="Add", width=30)
add_button.grid(column=1, columnspan=2, row=6)


window.mainloop()
