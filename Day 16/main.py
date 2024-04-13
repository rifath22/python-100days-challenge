from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

turn_on = True
espresso_menu_item      = MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5)
latte_menu_item         = MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5)
cappuccino_menu_item    = MenuItem(name="cappuccino", water=250, milk=100, coffee=24, cost=3.0)
# print(latte_menu_item.name)

menu = Menu()
# print(menu.get_items())
# print(menu.find_drink("cappuccino"))
# cappuccino = menu.find_drink("cappuccino")
# print(cappuccino.cost)
coffee_maker = CoffeeMaker()
# print(coffee_maker.report())
# print(coffee_maker.is_resource_sufficient(latte_menu_item))
# print(coffee_maker.make_coffee(latte_menu_item))

money_machine = MoneyMachine()
# print(money_machine.report())
# money_machine.make_payment(5.0)

while turn_on:
    user_input = str(input(f"What would you like? ({menu.get_items()}): ")).lower()
    if user_input == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_input == "off":
        turn_on = False
    else:
        requested_drink     = menu.find_drink(user_input)
        drink_cost          = requested_drink.cost
        sufficient_resource = coffee_maker.is_resource_sufficient(requested_drink)
        if sufficient_resource:
            payment = money_machine.make_payment(drink_cost)
            if payment:
                coffee_maker.make_coffee(requested_drink)
