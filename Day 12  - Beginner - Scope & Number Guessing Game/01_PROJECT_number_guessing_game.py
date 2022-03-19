import random

print('wewcome to the nyumbew guessewing game!!')
print('w-wange: 0-100 (incwuding 0 a-and 100)\n')
diff = input('choose a-a difficuwty:\n"easy" (6 lives) or "hard" (4 lives): ')


def game(lives):
    CORRECT_NUMBER = random.randint(1, 100)

    def high_or_low(guess):
        if guess > CORRECT_NUMBER:
            return 't-too high.'
        elif guess < CORRECT_NUMBER:
            return 't-too low.'
        else:
            return 'youw guess is cowwect'

    def start_game(CORRECT_NUMBER, lives):
        while lives > 0:
            print(f'\nyou have {lives} attempts wemaining.')
            guess = int(input('make a guess: '))
            guess_result = high_or_low(guess)
            print(guess_result)

            if guess_result == 'youw guess is cowwect':
                break

            print('g-guess again\n')
            lives -= 1

        print(f'\nthe cowwect num was {CORRECT_NUMBER} >_<')

    start_game(CORRECT_NUMBER, lives)


if diff == 'easy':
    game(6)
elif diff == 'hard':
    game(4)
else:
    print('i-input cowwect keywowds >_<')
