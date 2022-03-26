from functools import partial
from tkinter import Button, Canvas, Label, PhotoImage, Tk, messagebox
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE = 'French'

current_card = 'front'

# ------------ Random Index Not In Blacklisted List -----------#

data = pd.read_csv('data/french_words.csv')
language_words = data[LANGUAGE].to_list()
english_words = data['English'].to_list()

current_card_index = random.randint(0, len(language_words) - 1)

HIGHEST_SCORE = len(language_words)
current_score = 0


# -------------Change Card Functionality-----------#
def timer():
    window.after(3000, show_card)


def show_card(use_timer: bool = False):
    global current_card
    if current_card == 'front':
        canvas.itemconfig(card, image=back_card)
        canvas.itemconfig(language, text='English', fill='white')
        canvas.itemconfig(word,
                          text=english_words[current_card_index],
                          fill='white')
        current_card = 'back'
    else:
        canvas.itemconfig(card, image=front_card)
        canvas.itemconfig(language, text='French', fill='black')
        canvas.itemconfig(word,
                          text=language_words[current_card_index],
                          fill='black')
        current_card = 'front'

    if use_timer:
        timer()


# ---------------------------------------------------------------------#


def change_index(remove: bool = False):
    global current_card_index

    if remove:
        language_words.pop(current_card_index)
        english_words.pop(current_card_index)
        global current_score
        current_score += 1
        score['text'] = f'Score: {current_score}/{HIGHEST_SCORE}'

    try:
        current_card_index = random.randint(0, len(language_words) - 1)
    except ValueError:
        messagebox.showinfo(
            title='Congratulations',
            message=
            'Congratualations!!!!!\nYou have completed Flashuwu.\nPlease try again later >_<'
        )
    else:
        show_card(True)


# --------------------------UI-------------------------- #
window = Tk()
window.title('Flashuwu')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

score = Label(text=f'Score: {current_score}/{HIGHEST_SCORE}',
              pady=20,
              bg=BACKGROUND_COLOR,
              font=('Ariel', 20, 'normal'))
score.grid(row=0, column=1)

canvas = Canvas(width=800,
                height=526,
                bg=BACKGROUND_COLOR,
                highlightthickness=0)
front_card = PhotoImage(file='images/card_front.png')
back_card = PhotoImage(file='images/card_back.png')
card = canvas.create_image(400, 263, image=front_card)
language = canvas.create_text(390,
                              150,
                              text='French',
                              fill='black',
                              font=('Ariel', 30, 'italic'))
word = canvas.create_text(390,
                          300,
                          text=language_words[current_card_index],
                          fill='black',
                          font=('Ariel', 30, 'bold'))
canvas.grid(row=1, column=0, columnspan=2)

wrong_button_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(window,
                      image=wrong_button_image,
                      highlightthickness=0,
                      borderwidth=0,
                      command=partial(change_index, remove=False))
wrong_button.grid(row=2, column=0)

right_button_image = PhotoImage(file='images/right.png')
right_button = Button(window,
                      image=right_button_image,
                      highlightthickness=0,
                      borderwidth=0,
                      command=partial(change_index, remove=True))
right_button.grid(row=2, column=1)

timer()

window.mainloop()
