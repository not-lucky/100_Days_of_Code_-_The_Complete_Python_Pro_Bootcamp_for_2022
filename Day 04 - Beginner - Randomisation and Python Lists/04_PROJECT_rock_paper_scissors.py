rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
import random

rps = [rock, paper, scissors]

choice = int(input('nani do you choose? type 0 fow wock, ^•ﻌ•^ 1 f-fow papew o-ow 2 fow scissows. OwO\n'))

if choice > 2 or choice < 0:
    print('pwease chose a vawid nyumbew fwom t-the choices!')
else:
    print(f'\n\nYou chose:\n{rps[choice]}')

    comp_choice = random.randint(0, 2)
    print(f'\n\nComputer chose:\n{rps[comp_choice]}')

    draw = 'its a dwaw. XD'
    win = 'you won. XD'
    lose = 'you wose. XD'

    if choice == comp_choice:
        print(draw)
    elif choice == 0:
        if comp_choice == 1:
            print(lose)
        else:
            print(win)
    elif choice == 1:
        if comp_choice == 0:
            print(win)
        else:
            print(lose)
    else:
        if comp_choice == 0:
            print(lose)
        else:
            print(win)
