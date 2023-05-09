from tkinter import *
import pandas
from random import choice

current_card = {}
to_learn = {}
BACKGROUND_COLOR = "#B1DDC6"
FOREGROUND = '#FFFFFF'


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_image, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="#000")
    canvas.itemconfig(card_word, text=current_card['French'], fill="#000")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_image, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill=FOREGROUND)
    canvas.itemconfig(card_word, text=current_card['English'], fill=FOREGROUND)


def is_known():
    to_learn.remove(current_card)
    pandas.DataFrame(to_learn).to_csv('data/words_to_learn.csv', index=False)
    next_card()


try:
    to_learn = pandas.read_csv('data/words_to_learn.csv').to_dict(orient='records')
except FileNotFoundError:
    to_learn = pandas.read_csv('data/french_words.csv').to_dict(orient='records')


# ----- Setup window -----
window = Tk()
window.title('YAFcA - Yet Another Flashcard App')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')
card_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text='', font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text='', font=("Ariel", 60, "bold"))

check_image = PhotoImage(file='images/right.png')
cross_image = PhotoImage(file='images/wrong.png')
known_btn = Button(image=check_image, highlightthickness=0, command=is_known)
unknown_btn = Button(image=cross_image, highlightthickness=0, command=next_card)

canvas.grid(row=0, column=0, columnspan=2)
known_btn.grid(row=1, column=1)
unknown_btn.grid(row=1, column=0)

flip_timer = window.after(3000, flip_card)
next_card()
window.mainloop()
