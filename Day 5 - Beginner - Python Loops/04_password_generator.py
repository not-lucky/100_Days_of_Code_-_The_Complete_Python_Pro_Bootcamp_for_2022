#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("wewcome to the pypasswowd genewatow! >_<")
nr_letters= int(input("how many wettews wouwd you wike in y-youw passwowd?\n")) 
nr_symbols = int(input(f"how many symbows wouwd you wike?\n"))
nr_numbers = int(input(f"How many nyumbews would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#EASY LEVEL---
password = ''
for i in range(nr_letters):
    password += letters[random.randint(0, len(letters) - 1)]

for i in range(nr_symbols):
    password += symbols[random.randint(0, len(symbols) - 1)]

for i in range(nr_numbers):
    password += numbers[random.randint(0, len(numbers) - 1)]

print(password)


#HARD LEVEL---
password_copy = list(password)
random_password = []
for i in range(len(password_copy)):
    rand = random.randint(0, len(password_copy) - 1)
    random_password.append(password_copy[rand])
    password_copy.pop(rand)

print(''.join(random_password))
