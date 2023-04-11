from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
DEFAULT_USERNAME = 'ajm27'
global data
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_list = []
    password_list.extend([choice(letters) for _ in range(randint(8, 10))])
    password_list.extend([choice(numbers) for _ in range(randint(2, 4))])
    password_list.extend([choice(symbols) for _ in range(randint(2, 4))])

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    data_valid = False
    # Retrieve Data
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {website: {'username': username,
                          'password': password}}
    global data
    # Validate Data
    if website == '' or username == '' or password == '':
        messagebox.showerror(title='Error', message='All fields are required!')
    else:
        try:
            data_file = open('data.json', 'r')
        except FileNotFoundError:
            data = new_data
        else:
            data = json.load(data_file)
            data.update(new_data)
        finally:
            data_file = open('data.json', 'w')
            json.dump(data, data_file, indent=4)
            data_file.close()
    # Save Data to File
    pyperclip.copy(password)
    messagebox.showinfo(title='Password Saved!', message='Password saved to database and copied to clipboard!')
    # Reset Form
    website_entry.delete(0, END)
    username_entry.delete(0, END)
    username_entry.insert(0, DEFAULT_USERNAME)
    password_entry.delete(0, END)


def search():
    global data
    try:
        with open('data.json') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title='File Not Found', message='Existing data not found.')
    else:
        try:
            website = website_entry.get()
            username = data[website]['username']
            password = data[website]['password']
        except KeyError:
            messagebox.showerror(title='Website Not Found', message=f'{website} not found in database.')
        else:
            messagebox.showinfo(title=f'{website}', message=f"Username: {username}\nPassword:{password}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

# Canvas Setup
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)

# Label Setup
website_lbl = Label(text='Website:')
username_lbl = Label(text='Email/Username:')
password_lbl = Label(text='Password:')

# Entry Setup
website_entry = Entry(width=35)
username_entry = Entry(width=35)
password_entry = Entry(width=25)

# Button Setup
gen_password_btn = Button(text='Generate Password', command=generate_password)
add_btn = Button(text='Add', width=29, command=save)
search_btn = Button(text='Search', command=search)

# Grid Layout
canvas.grid(row=0, column=1)

website_lbl.grid(row=1, column=0)
username_lbl.grid(row=2, column=0)
password_lbl.grid(row=3, column=0)

website_entry.grid(row=1, column=1)
username_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1)

gen_password_btn.grid(row=3, column=2)
add_btn.grid(row=4, column=1, columnspan=2)
search_btn.grid(row=1, column=2)

website_entry.focus()
username_entry.insert(0, DEFAULT_USERNAME)

window.mainloop()
