from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


def coffee_machine():
    while True:
        choose = input(f'What would you like: ({menu.get_items()})').lower()

        if choose == 'report':
            coffee_maker.report()
            money_machine.report()
        elif choose == 'off':
            break
        else:
            drink = menu.find_drink(choose)
            if drink is not None:
                if coffee_maker.is_resource_sufficient(drink):
                    if money_machine.make_payment(drink.cost):
                        coffee_maker.make_coffee(drink)


coffee_machine()
