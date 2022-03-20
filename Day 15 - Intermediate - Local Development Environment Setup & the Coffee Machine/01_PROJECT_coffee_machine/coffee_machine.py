from data import MENU

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money': 0.0
}


def give_report():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${resources["money"]}')


def enough_money(drink):
    print('Please insert coins.')
    money_received = 0
    money_received += int(input('How many quarters?: ')) * 25
    money_received += int(input('How many dimes?: ')) * 10
    money_received += int(input('How many nickel?: ')) * 5
    money_received += int(input('How many pennies?: ')) * 1
    if money_received >= MENU[drink]['cost']:
        change = money_received / 100 - MENU[drink]['cost']
        return True, change

    return False, money_received


def enough_resource(drink):
    for ingredient in MENU[drink]['ingredients']:
        # print(ingredient)
        # print(resources[ingredient])
        # print(MENU[drink]['ingredients'][ingredient])
        if resources[ingredient] < MENU[drink]['ingredients'][ingredient]:
            return False
    return True


def update_resources(drink):
    global resources
    for key in MENU[drink]['ingredients']:
        resources[key] -= MENU[drink]['ingredients'][key]
    resources['money'] += MENU[drink]['cost']


def coffee_machine():
    while True:
        choose = input('What would you like: (espresso/latte/cappuccino/report/off)').lower()

        if choose == 'report':
            give_report()
        elif choose == 'off':
            print('Coffee machine is Turning off.')
            return
        else:
            is_enough_resource = enough_resource(choose)
            if not is_enough_resource:
                print('Sorry machine does not have enough resources left.')
            else:
                enough_money_received = enough_money(choose)
                if enough_money_received:
                    print(f'Here is ${enough_money_received[1]} in change.')
                    print(f'Here is your {choose}. Enjoy!')
                    update_resources(choose)
                else:
                    print('Sorry that is not enough money. Money refunded.')


coffee_machine()
