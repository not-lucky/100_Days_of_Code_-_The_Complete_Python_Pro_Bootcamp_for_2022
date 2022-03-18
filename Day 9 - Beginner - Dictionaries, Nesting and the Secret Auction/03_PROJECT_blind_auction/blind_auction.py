# from replit import clear
#HINT: You can call clear() to clear the output in the console.

import art
print(art.logo)

auction = {}

print('wewcome to the secwet auction pwogwam. >_<\n\n\n')
while True:
	name = input('entew youw nyame pwease. >_<\n')
	bid = int(input('\n\nentew youw bid pwease. XD\n'))

	auction[name] = bid

	if input('\n\n\nawe thewe any othew biddews?\nyes o-ow nyo\n') == 'nyo':
		break


highest_bid = 0
highest_bidder = ''
for key in auction:
	if auction[key] > highest_bid:
		highest_bid = auction[key]
		highest_bidder = key

print(f'\n\n\n\nthe winnew of the secwet auction p-pwogwam is {highest_bidder} with a-a bid of {auction[highest_bidder]}')