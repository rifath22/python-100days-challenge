from data import MENU, resources
machine_on = True
money = 0

def check_resources(flavor_type):
    ingredients = MENU[flavor_type]['ingredients']
    for key in ingredients:
        if ingredients[key] > resources[key]:
            print(f" Sorry there is not enough {key}")
            return False
    return True
    
def modify_resources(flavor_type, change_direction):
    ingredients = MENU[flavor_type]['ingredients']
    if change_direction == "add":
        for key in ingredients:
            resources[key] = resources[key] + ingredients[key]
    else:
        for key in ingredients:
            resources[key] = resources[key] - ingredients[key]

def process_transaction(flavor_type):
    global money
    print("Please insert coins.")
    quaters     = int(input("How many quaters?: "))
    dimes       = int(input("How many dimes?: "))
    nickles     = int(input("How many nickles?: "))
    pennies     = int(input("How many pennies?: "))
    user_amount = (quaters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)

    if user_amount >= MENU[flavor_type]['cost']:
        money = round(money + MENU[flavor_type]['cost'], 2)
        change_amount = round(user_amount - MENU[flavor_type]['cost'], 2)
        print(f"Here is ${change_amount} in change")
        print(f"Here is your {flavor_type} Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")
        modify_resources(flavor_type, "add")

while machine_on:
    user_input = str(input("What would you like? (espresso/latte/cappucino): "))
    if user_input == "report":
        water   = resources["water"]
        milk    = resources["milk"]
        coffee  = resources["coffee"]
        print(f"Water: {water} ml")
        print(f"Milk: {milk} ml")
        print(f"Coffee: {coffee} g")
        print(f"Money: ${money}")
    elif user_input == "latte":
        enough_resources = check_resources(user_input)
        if enough_resources:
            modify_resources(user_input, "sub")
            process_transaction(user_input)
    elif user_input == "espresso":
        enough_resources = check_resources(user_input)
        if enough_resources:
            modify_resources(user_input, "sub")
            process_transaction(user_input)
    elif user_input == "cappuccino":
        enough_resources = check_resources(user_input)
        if enough_resources:
            modify_resources(user_input, "sub")
            process_transaction(user_input)
    elif user_input == "off":
        machine_on = False
