from tkinter import *


def button_click():
	my_label.config(text=input.get())


window = Tk()
window.title("gui gui gummy gui")
window.minsize(width=400, height=300)
window.config(padx=50, pady=50)

my_label = Label(text="Click the button!", font=("Arial", 20, "bold"))
my_label.grid(column=0, row=0)

button = Button(text="Click me!", command=button_click)
button.grid(column=1, row=1)

button = Button(text="I'm a new button!", command=button_click)
button.grid(column=2, row=0)

input = Entry()
input.grid(column=3, row=3)

window.mainloop()
