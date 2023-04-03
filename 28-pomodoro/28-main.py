from tkinter import *
from math import floor
reps = 1
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 3
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 2
DELAY = 10

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_cntdwn():
    global reps
    if reps % 2:
        check_label.config(text=reps)
        countdown(WORK_MIN * 60)
    elif reps == 8:
        countdown(LONG_BREAK_MIN * 60)
        reps = 1
    else:
        countdown(SHORT_BREAK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    global reps
    display_string = f'{floor(count / 60):02d}:{count % 60:02d}'
    canvas.itemconfig(timer_text, text=display_string)
    if count > 0:
        canvas.after(DELAY, countdown, count - 1)
    else:
        reps += 1
        start_cntdwn()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
title_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, 'bold'))
start_btn = Button(text='Start', command=start_cntdwn)
reset_btn = Button(text='Reset')
check_label = Label(text='check', fg=GREEN, bg=YELLOW, font=('Courier', 14))

title_label.grid(row=0, column=1)
canvas.grid(row=1, column=1)
start_btn.grid(row=2, column=0)
reset_btn.grid(row=2, column=2)
check_label.grid(row=3, column=1)


window.mainloop()
