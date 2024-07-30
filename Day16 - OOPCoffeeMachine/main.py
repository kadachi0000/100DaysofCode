from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

mr_coffee = CoffeeMaker()
menu = Menu()
process_payment = MoneyMachine()

active = True
while active:
    options = menu.get_items()
    order = input(f"What would you like to drink? {options}: ")
    if order == "report":
        mr_coffee.report()
        process_payment.report()
    elif order == "off":
        active = False
    else:
        drink = menu.find_drink(order)
        if mr_coffee.is_resource_sufficient(drink) and process_payment.make_payment(drink.cost):
            mr_coffee.make_coffee(drink)
