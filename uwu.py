############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card():
	return random.choice(cards)


def blackjack(you, comp):
	if sum(you) == 21 and sum(comp) == 21:
		return 'You both hit a blackJAKC????!!!! WOW Its a draw though'
	elif sum(you) == 21:
		return 'You hit a blackjack!!! YOu win.'
	elif sum(comp) == 21:
		return 'comp balckkac. you lose.'

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

def game():
	print(you, 'and the sum  ', sum(you),'\n',comp)
	if sum(you) > 21:
		if bust_or_continue(you):
			print('over 21dgdgdgd')
			return
		else:
			you[you.index(11)] = 1

	print(you, 'and the sum  ', sum(you),'\n',comp)
	if sum(you) == 21 or sum(comp) == 21:
		print(blackjack(you, comp))
		return



	more_cards_or_not = input("Type 'y' to get another card, type 'n' to pass: ")
	if more_cards_or_not == 'y':
		you.append(draw_card())
		game()
		return
	else:
		while sum(comp) < 17:
			comp.append(draw_card())

		if sum(comp) > 21:
			print('comp more than 21. u win', comp)
			return
		else:
			if sum(you) == sum(comp):
				print(you, comp)
				print('draw')
				return
			elif sum(you) > sum(comp):
				print(you, comp)
				print('i win')
				return
			else:
				print(you, comp)
				print('comp win')
				return

while input('Wanna try a game of Blackjack? ') == 'y':
	you = []
	comp = []
	for i in range(2):
		you.append(draw_card())
		comp.append(draw_card())
	game()