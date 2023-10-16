from tkinter import *

# window = Tk()
# window.title("GUI Program")
# window.minsize(width=500, height=300)
# window.config(padx=30, pady=30)
#
# # Labels
# my_label = Label(text="I am a label", font=('Arial', 24, 'bold'))
# my_label.grid(row=0, column=0)
# # my_label['text'] = 'Updated text'
#
# # Buttons
#
#
# def button_clicked():
#     my_label.config(text=txt_input.get())
#
#
# my_btn = Button(text='click me', command=button_clicked)
# my_btn.grid(row=1, column=1)
#
# # Entry
# txt_input = Entry(width=10)
# txt_input.grid(row=2, column=3)
#
# new_btn = Button(text='2nd button')
# new_btn.grid(row=0, column=2)
#
# window.mainloop()

# # Positional Arguments
# def add(*args):
#     sum1 = 0
#     for n in args:
#         sum1 += n
#     return sum1
#
#
# print(add(3, 2, 4, 5, 1, 5, 2))

# # Keyword Arguments (and positional arguments)
#
# def calculate(*args, **kwargs):
#     result = 0
#     if kwargs['method'] == 'add':
#         for n in args:
#             result += n
#     if kwargs['method'] == 'mult':
#         result = args[0]
#         for n in range(1, len(args)):
#             result *= args[n]
#     return result
#
#
# print(calculate(3, 5, 10, method='mult'))
# print(calculate(3, 5, 10, method='add'))

MILES_TO_KM = 1.609


def button_calculate():
    mid_label['text'] = f'is equal to {float(miles_entry.get()) * MILES_TO_KM:0.2f} Km'


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=225, height=120)
window.config(padx=30, pady=30)
my_font = ('Aria', 12)

miles_label = Label(text='Miles', font=my_font)
mid_label = Label(text='is equal to 0 Km', font=my_font)

calc_button = Button(text='Calculate', command=button_calculate)

miles_entry = Entry(width=6)

miles_entry.grid(column=0, row=0)
miles_label.grid(column=1, row=0)
mid_label.grid(row=1, column=0, columnspan=2)
calc_button.grid(column=0, row=2)


window.mainloop()




# # Example tkinter widgets
# from tkinter import *

# Creating a new window and configurations
# window = Tk()
# window.title("Widget Examples")
# window.minsize(width=500, height=500)
#
# #Labels
# label = Label(text="This is old text")
# label.config(text="This is new text")
# label.pack()
#
# #Buttons
# def action():
#     print("Do something")
#
# #calls action() when pressed
# button = Button(text="Click Me", command=action)
# button.pack()
#
# #Entries
# entry = Entry(width=30)
# #Add some text to begin with
# entry.insert(END, string="Some text to begin with.")
# #Gets text in entry
# print(entry.get())
# entry.pack()
#
# #Text
# text = Text(height=5, width=30)
# #Puts cursor in textbox.
# text.focus()
# #Adds some text to begin with.
# text.insert(END, "Example of multi-line text entry.")
# #Get's current value in textbox at line 1, character 0
# print(text.get("1.0", END))
# text.pack()
#
# #Spinbox
# def spinbox_used():
#     #gets the current value in spinbox.
#     print(spinbox.get())
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
# #Scale
# #Called with current scale value.
# def scale_used(value):
#     print(value)
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
# #Checkbutton
# def checkbutton_used():
#     #Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
# #variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()
#
# #Radiobutton
# def radio_used():
#     print(radio_state.get())
# #Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
#
# #Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#
# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
# window.mainloop()