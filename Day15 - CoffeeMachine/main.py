from data import resources, MENU
import sys


def place_order():
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        sys.exit()
    elif order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {resources['money']}")
        sys.exit()
    else:
        return order


def check_ingredients(order):
    for resource in MENU[order]["ingredients"]:
        needed_ingredient_level = MENU[order]['ingredients'][resource]
        ingredient_total = resources[resource]
        if needed_ingredient_level > ingredient_total:
            print(f"Not enough {resource}.")
            sys.exit()
        else:
            return True


def pay_order(order):
    cost = float(MENU[order]["cost"])
    formatted_cost = '${:,.2f}'.format(MENU[order]["cost"])
    print(f"A {order} costs {formatted_cost}. Please insert your coins.")
    quarters = int(input("How many quarters will you insert? "))
    quarters_total = float(quarters * .25)
    dimes = int(input("How many dimes will you insert? "))
    dimes_total = float(dimes * .10)
    nickels = int(input("How many nickels will you insert? "))
    nickels_total = float(nickels * .05)
    pennies = int(input("How many pennies will you insert? "))
    pennies_total = float(pennies * .01)
    total_paid = quarters_total + dimes_total + nickels_total + pennies_total
    change = total_paid - cost

    if change >= 0:
        formatted_change = '${:,.2f}'.format(change)
        resources["money"] = formatted_cost
        print(f"Here is {formatted_change} in change.")
    else:
        print("You do not have enough money. Please try again.")
        sys.exit()


def update_resources_total(order):
    for resource in MENU[order]["ingredients"]:
        used_ingredient = MENU[order]['ingredients'][resource]
        ingredient_total = resources[resource]
        ingredient_total -= used_ingredient
        resources[resource] = ingredient_total


def main():
    order = ""
    while order != "off":
        order = place_order()
        check_ingredients(order)
        pay_order(order)
        update_resources_total(order)
        print(f"Here is your {order}. Enjoy!")


main()
