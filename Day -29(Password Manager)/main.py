from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_letters)]
    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

    # print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(
            title=password, message=f"You left the find empty\n Website: {website}\n Password: {password}\n")
    else:
        is_ok = messagebox.askokcancel(
            title=website, message=f"Do you want to save the password? \n Email: {email} \n Password: {password} \n")
        if is_ok:
            if len(password) > 0:
                with open('pass.txt', 'a') as f:  # Use 'a' for append mode
                    f.write(f"{website} | {email} | {password}\n")
                    # Clear the entry widgets
                    website_input.delete(0, 'end')
                    password_input.delete(0, 'end')


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
website_input.focus()
# website_input.get()
website_input.grid(column=1, columnspan=2, row=3)


email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=4)

email_input = Entry(width=35)
# email_input.get()

email_input.grid(column=1, columnspan=2, row=4)
email_input.insert(0, "example@gamil.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=5)

password_input = Entry(width=40)
# password_input.get()
password_input.grid(column=1, columnspan=2, row=5)


generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=8, row=5)

add_button = Button(text="Add", width=30, command=save)
add_button.grid(column=1, columnspan=2, row=6)


window.mainloop()
