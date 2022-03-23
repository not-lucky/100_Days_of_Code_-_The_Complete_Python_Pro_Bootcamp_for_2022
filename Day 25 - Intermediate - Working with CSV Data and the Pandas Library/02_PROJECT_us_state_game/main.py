import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('U.S. State Game')

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
user = turtle.Turtle()
user.hideturtle()
user.penup()
user.speed(0)

data = pd.read_csv('50_states.csv')
states = data['state'].to_list()
coordinates = data[['x', 'y']].to_dict()

guessed_states = set()
while len(guessed_states) < 50:
    answer = screen.textinput(title=f'{len(guessed_states)}/50 Guess the state',
                              prompt='Guess the state').title()
    
    if answer == 'Exit':
        break
    print(answer)
    if answer in states:
        guessed_states.add(answer)
        state_index = states.index(answer)
        x_coor_of_state = coordinates['x'][state_index]
        y_coor_of_state = coordinates['y'][state_index]
        user.goto(x_coor_of_state, y_coor_of_state)
        user.write(answer)

states = set(states)
not_guessed_states = sorted(list(states.difference(guessed_states)))
pd.DataFrame(not_guessed_states).to_csv('not_guessed_states.csv')
