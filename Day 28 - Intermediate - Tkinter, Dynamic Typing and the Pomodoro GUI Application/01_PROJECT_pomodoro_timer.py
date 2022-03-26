from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_mech = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():

    canvas.after_cancel(timer_mech)
    title_label.config(text='Timer', fg=GREEN)
    checkmark.config(text='')
    canvas.itemconfig(timer, text='00:00')

    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM -------------------------------#
def start_timer():
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    global reps
    reps += 1

    if reps % 2 != 0:
        title_label.config(text='Work', fg=GREEN)
        countdown(work_sec)
    else:
        if reps % 8 != 0:
            title_label.config(text='Break', fg=PINK)
            checkmark['text'] += '✓'
            countdown(short_break_sec)
        else:
            title_label.config(text='Break', fg=RED)
            checkmark['text'] += '✓'
            countdown(long_break_sec)


# ------------------------- COUNTDOWN MECHANISM ----------------------------#


def countdown(count):
    count_min = count // 60
    count_sec = count % 60

    canvas.itemconfig(timer, text=f'{count_min:0>2}:{count_sec:0>2}')
    if count > 0:
        global timer_mech
        timer_mech = window.after(1000, countdown, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
imagee = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=imagee)
timer = canvas.create_text(100,
                           130,
                           text='00:00',
                           fill='white',
                           font=(FONT_NAME, 24, 'bold'))
canvas.grid(column=1, row=1)

title_label = Label(text='Timer',
                    fg=GREEN,
                    bg=YELLOW,
                    font=(FONT_NAME, 34, 'bold'))
title_label.grid(column=1, row=0)

start_button = Button(text='Start', command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

checkmark = Label(text='', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 16, 'normal'))
checkmark.grid(column=1, row=3)

window.mainloop()
