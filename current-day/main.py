from tkinter import *
BACKGROUND = "#000000"
MIDGROUND = '#888888'
FOREGROUND = '#FFFFFF'

# ----- Setup window -----
window = Tk()
window.title('YAFcA - Yet Another Flashcard App')
window.config(padx=25, pady=45, bg=BACKGROUND)

canvas = Canvas(width=250, height=175, bg=MIDGROUND, highlightthickness=0)
known_btn = Button(text='Known')
unknown_btn = Button(text='Unknown')

canvas.grid(row=0, column=1)
known_btn.grid(row=1, column=2)
unknown_btn.grid(row=1, column=0)
window.mainloop()
