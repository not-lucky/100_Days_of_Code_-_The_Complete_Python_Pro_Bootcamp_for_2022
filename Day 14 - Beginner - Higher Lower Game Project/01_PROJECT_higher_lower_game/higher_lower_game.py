import random

import art
from game_data import data


# import os

# def cls():
#     os.system('cls' if os.name=='nt' else 'clear')

# # now, to clear the screen


def get_person():
    return random.choice(data)


def setup(score):
    print(art.logo)
    if score != 0:
        print(f'You\'re right! Current score: {score}.')
    per1 = get_person()
    print(f"Compare A: {per1['name']}, a {per1['description']}, from {per1['country']}.", end='')
    print(art.vs)
    per2 = get_person()

    while per1 == per2:
        per2 = get_person()
    print(f"Against B: {per2['name']}, a {per2['description']}, from {per2['country']}.")

    return per1['follower_count'], per2['follower_count']


def winner_A_OR_B(followers):
    if followers[0] > followers[1]:
        return 'A'
    else:
        return 'B'


def game():
    score = 0

    while True:
        followers_in_tuple = setup(score)
        print(followers_in_tuple)
        winner = winner_A_OR_B(followers_in_tuple)

        choose = input('Who has more followers?\nType "A" or "B": ').lower()

        if choose == winner.lower():
            score += 1
        # cls()

        else:
            print(f'Sorry, thats\'s wrong. Final score: {score}.')
            break


game()
