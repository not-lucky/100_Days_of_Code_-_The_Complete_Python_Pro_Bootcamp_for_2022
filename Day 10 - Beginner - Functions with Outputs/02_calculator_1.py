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

num1 = int(input('first num:\n'))

for operator in operations:
    print(operator)

operation_symbol = input('pick anb operation froima bove\n')
num2 = int(input('sefcond num:\n'))

answer = operations[operation_symbol](num1, num2)

print(f'{num1} {operation_symbol} {num2} = {answer}')
