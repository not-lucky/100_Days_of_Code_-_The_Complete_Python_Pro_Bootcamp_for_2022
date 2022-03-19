import random

import art

print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def draw_card():
    return random.choice(cards)


def blackjack(you, comp):
    if sum(you) == 21 and sum(comp) == 21:
        return 'd'
    elif sum(you) == 21:
        return 'w'
    elif sum(comp) == 21:
        return 'l'


def bust_or_continue(you):
    if 11 not in you:
        return True
    else:
        temp_you = you * 1
        index_of_11 = you.index(11)
        temp_you[index_of_11] = 1
        if sum(temp_you) > 21:
            return True
    return False


def result_for_you():
    return f"\nYour cards: {you}, sum {sum(you)}\nComputer's first card: {comp[0]}"


def result_for_all(you, comp):
    return f"\nYour cards: {you}, Final Sum {sum(you)}\nComputer's final hand: {comp}, Final Sum: {sum(comp)}"


def game():
    print(result_for_you())

    if sum(you) > 21:
        if bust_or_continue(you):
            return 'l'
        else:
            you[you.index(11)] = 1

    if sum(you) == 21 or sum(comp) == 21:
        print()
        return blackjack(you, comp)

    more_cards_or_not = input("Type 'y' to get another card, type 'n' to pass: ")
    if more_cards_or_not == 'y':
        you.append(draw_card())
        return game()

    else:
        while sum(comp) < 17:
            comp.append(draw_card())

        if sum(comp) > 21:
            print('comp more than 21. u win', comp)
            return 'w'
        else:
            if sum(you) == sum(comp):
                print(you, comp)
                return 'd'
            elif sum(you) > sum(comp):
                print(you, comp)
                return 'w'
            else:
                print(you, comp)
                return 'l'


while input('\n\n\nWanna try a game of Blackjack?\nType "y" if yes or basically anything if no:\n') == 'y':
    you = []
    comp = []
    for _ in range(2):
        you.append(draw_card())
        comp.append(draw_card())
    result_of_game = game()
    # print(result_of_game)
    if result_of_game == 'w':
        print(f'{result_for_all(you, comp)}\nCongratulations!!! You won.')
    elif result_of_game == 'l':
        print(f'{result_for_all(you, comp)}\nAHHH!! gg though')
    else:
        print(f'{result_for_all(you, comp)}\nRIP draw')
