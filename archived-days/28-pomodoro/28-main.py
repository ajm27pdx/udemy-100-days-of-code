from tkinter import *
from math import floor
reps = 1
timer = None
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 2
DELAY = 10 #1000

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global timer, reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config('Timer')
    check_label.config('')
    reps = 1

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_cntdwn():
    global reps
    if reps % 2:
        if reps == 7:
            check_label.config(text='✔✔✔')
        elif reps == 5:
            check_label.config(text='✔✔')
        elif reps == 3:
            check_label.config(text='✔')
        title_label.config(text='Working', fg=GREEN)
        countdown(WORK_MIN * 60)
    elif reps == 8:
        title_label.config(text='Long Break', fg=RED)
        countdown(LONG_BREAK_MIN * 60)
        check_label.config(text='')
    else:
        title_label.config(text='Short Break', fg=PINK)
        countdown(SHORT_BREAK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    global reps, timer
    display_string = f'{floor(count / 60):02d}:{count % 60:02d}'
    canvas.itemconfig(timer_text, text=display_string)
    if count > 0:
        timer = canvas.after(DELAY, countdown, count - 1)
    else:
        reps += 1
        if reps <= 8:
            start_cntdwn()
        else:
            reps = 1


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
title_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, 'bold'), width=12)
start_btn = Button(text='Start', command=start_cntdwn)
reset_btn = Button(text='Reset', command=reset_timer)
check_label = Label(text='', fg=GREEN, bg=YELLOW, font=('Courier', 14))

title_label.grid(row=0, column=1)
canvas.grid(row=1, column=1)
start_btn.grid(row=2, column=0)
reset_btn.grid(row=2, column=2)
check_label.grid(row=3, column=1)


window.mainloop()
