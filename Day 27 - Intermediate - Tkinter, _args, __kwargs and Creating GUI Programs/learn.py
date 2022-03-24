from tkinter import Button, Tk, Label, Entry

window = Tk()
window.title('hmmmmmm')
window.minsize(width=800, height=600)

label = Label(text='am a label', font=('Arial', 24, 'bold'))
label.grid(column=0, row=0)


def change_label():
    label['text'] = input.get()


button = Button(text='click me',
                command=change_label,
                font=('Arial', 20, 'normal'))
button.grid(column=1, row=1)

new_button = Button(text='new button')
new_button.grid(column=2, row=0)

input = Entry(width=50)
input.grid(column=3, row=2)

window.mainloop()
