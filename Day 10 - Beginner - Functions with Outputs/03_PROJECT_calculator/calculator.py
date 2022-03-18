
def add(n1, n2):
	return n1 + n2

def subtract(n1, n2):
	return n1 - n2

def multiply(n1, n2):
	return n1 * n2

def divide(n1, n2):
	return n1 / n2


operations = {
	'+': add,
	'-': subtract,
	'*': multiply,
	'/': divide
}


def calculator():
	num1 = float(input('entew the fiwst numbew:\n'))
	for operator in operations:
		print(operator)

	while True:
		operation_symbol = input('entew one o-of the opewatow d-dispwaying above:\n')
		num2 = float(input('e-entew the n-nyext nyumbew:\n'))

		answer = operations[operation_symbol](num1, num2)



		print(f'{num1} {operation_symbol} {num2} = {answer}')

		choose = input(f"d-do you want to have f-fuwthew cawcuwation w-with {answer} , \
p-pwess 'y' if yes, σωσ 'n' to quit the cawcuwatow, and 's' to stawt cawcuwations aww o-ovew again\n")

		if choose == 's':
			calculator()
			break
		elif choose == 'n':
			break
		elif choose == 'y':
			num1 = answer

calculator()