from tkinter import Tk, Label, Entry, Button

FONT = ('Arial', 20, 'normal')

window = Tk()
window.title('Miles to Kilometers Converter')
window.minsize(width=400, height=300)
window.config(padx=30, pady=30)

mile = Entry()
mile.config(width=20)
mile.grid(column=1, row=0)
mile.focus()

label1 = Label(text='miles', font=FONT, padx=20)
label1.grid(column=2, row=0)

label2 = Label(text='is equal to', font=FONT, padx=20)
label2.grid(column=0, row=1)


def mi_to_kilo():
    # print(type(mile.get()))
    label3['text'] = round(float(mile.get()) * 1.609344, 3)


label3 = Label(text=0, font=FONT)
label3.grid(column=1, row=1)

label4 = Label(text='kilometers', font=FONT, padx=20)
label4.grid(column=2, row=1)

button = Button(text='Calculate', command=mi_to_kilo)
button.grid(column=1, row=2)

window.mainloop()
