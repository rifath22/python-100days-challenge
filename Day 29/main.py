import tkinter
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]
    print(f"password_list: {password_list} ")

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    print(f"Your password is: {password}")
    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_to_file():
    website_entry = website_input.get()
    email_entry = email_input.get()
    password_entry = password_input.get()

    if len(website_entry) == 0 or len(email_entry) == 0 or len(password_entry) == 0:
        messagebox.showinfo(title="oops", message="You left something empty")
    else:
        add_new_entry_to_file = f"{website_entry} | {email_entry} | {password_entry}\n"
        # print(f"{website_entry} | {email_entry} | {password_entry}\n")

        is_ok = messagebox.askokcancel(title=website_entry, message=f"Email: {email_entry}\nPassword: {password_entry}\n Is it ok to save?")
        if is_ok:
            with open("./passwords.txt", mode='a') as out_file:
                out_file.write(add_new_entry_to_file)
                website_entry = website_input.delete(0, tkinter.END)
                password_entry = password_input.delete(0, tkinter.END)
# ---------------------------- UI SETUP ---------------------------
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
logo_img = tkinter.PhotoImage(file='./logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0,column=0, rowspan=4, columnspan=4)

#Labels
website_label = tkinter.Label(text="Website: ")
website_label.grid(row=4,column=0)

email_label = tkinter.Label(text="Email/Username: ")
email_label.grid(row=5,column=0)

password_label = tkinter.Label(text="Password: ")
password_label.grid(row=6,column=0)

#Button

password_button = tkinter.Button(text="Generate Password", command=password_generator)
password_button.grid(row=6,column=2)
add_button = tkinter.Button(text="add", command=add_to_file, width=36)
add_button.grid(row=7,column=1, columnspan=2)

#Entry
website_input = tkinter.Entry(width=41)
website_input.grid(row=4,column=1, columnspan=2)
email_input = tkinter.Entry(width=41)
email_input.grid(row=5,column=1, columnspan=2)
email_input.insert(0, "mailmerifath@gmail.com")
password_input = tkinter.Entry(width=21)
password_input.grid(row=6,column=1)


window.mainloop()