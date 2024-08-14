from tkinter import *


def convert():
	miles_amount = float(miles_input.get())
	km_amount = round(miles_amount * 1.609)
	km_amount_label.config(text=f"{km_amount}")


window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=300, height=150)
window.config(padx=50, pady=30)

button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

km_amount_label = Label(text="0")
km_amount_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

window.mainloop()
