import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json

# -------------------------- PASSWORD GENERATOR ----------------------------- #
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def gen_password():
    # nr_letters = random.randint(7, 12)
    # nr_symbols = random.randint(5, 10)
    # nr_numbers = random.randint(5, 10)

    my_password = random.choices(letters, k=random.randint(
        7, 12)) + random.choices(numbers, k=random.randint(
            5, 10)) + random.choices(symbols, k=random.randint(5, 10))
    random.shuffle(my_password)
    joined_password = ''.join(my_password)
    password_entry.insert(END, joined_password)
    pyperclip.copy(joined_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password_to_file():
    site = site_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    data = {
        site: {
            'email': email,
            'password': password,
        },
    }

    if len(site) < 1 or len(email) < 1 or len(password) < 1:
        messagebox.showinfo(title='Error',
                            message='Please fill out all the fields.')
        return

    save = messagebox.askokcancel(
        title=site,
        message=
        f'These are the details entered.\nSite: {site}\nEmail: {email}\nPassword: {password}\nDo you want to save these?'
    )

    if save:
        try:
            with open('passwords.json', 'r') as fl:
                new_data = json.load(fl)

        except FileNotFoundError:
            with open('passwords.json', 'w') as fl:
                json.dump(data, fl, indent=4)

        else:
            new_data.update(data)

            with open('passwords.json', 'w') as fl:
                json.dump(new_data, fl, indent=4)

        finally:
            site_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- Search -----------------------------------#
def search_json_file():
    try:
        with open('passwords.json', 'r') as fl:
            new_data = json.load(fl)

    except FileNotFoundError:
        messagebox.showerror(title='Error', message='No data file found.')

    else:
        try:
            site_data = new_data[site_entry.get()]
        except KeyError:
            messagebox.showerror(
                title='Error',
                message=f'No datails for {site_entry.get()} found.')
        else:
            messagebox.showinfo(
                title=site_entry.get(),
                message=
                f'Email: {site_data["email"]}\nPassword: {site_data["password"]}'
            )


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=40)

canvas = Canvas(width=200, height=190, highlightthickness=0)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 85, image=logo)
canvas.grid(column=1, row=0)

site_label = Label(text='Website:')
site_label.grid(column=0, row=1)

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

pass_label = Label(text='Password:')
pass_label.grid(column=0, row=3)

site_entry = Entry(width=32)
site_entry.grid(column=1, row=1)
site_entry.focus()

email_entry = Entry(width=51)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(END, 'not-lucky@email.domain')

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

search = Button(text='Search', width=14, command=search_json_file)
search.grid(column=2, row=1)

gen_pass = Button(text='Generate Password', command=gen_password)
gen_pass.grid(column=2, row=3)

add = Button(text='Add', width=43, command=save_password_to_file)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()
