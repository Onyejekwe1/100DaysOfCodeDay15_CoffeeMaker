MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
WATER_RESOURCE = resources['water']
MILK_RESOURCE = resources['milk']
COFFEE_RESOURCE = resources['coffee']

profit = 0
is_coffee = True


while is_coffee:

    def prepare_order(coffee_type):
        water = MENU[coffee_type]['ingredients']['water']

        if coffee_type == "espresso":
            milk = 0
        else:
            milk = MENU[coffee_type]['ingredients']['milk']
        coffee = MENU[coffee_type]['ingredients']['coffee']
        cost = MENU[coffee_type]['cost']
        global profit

        if WATER_RESOURCE < water:
            return f"Sorry there is not enough water."
        elif MILK_RESOURCE < milk:
            return f"Sorry there is not enough milk"
        elif COFFEE_RESOURCE < coffee:
            return f"Sorry there is not enough coffee"

        quarters = int(input("insert quarter coins: "))
        dimes = int(input("insert dime coins: "))
        nickles = int(input("insert nickle coins: "))
        pennies = int(input("insert penny coins: "))

        total_amount = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)

        if total_amount < cost:
            print("Sorry that's not enough money. Money refunded.")
            return ""

        if total_amount > cost:
            print(f"Here is ${round(total_amount - cost, 2)} dollars in change.")

        profit += cost
        make_coffee(water, milk, coffee, coffee_type)
        print(f"Here is your {coffee_type}. Enjoy!.")
        return ""


    def make_coffee(water, milk, coffee, coffee_type):
        global WATER_RESOURCE
        global COFFEE_RESOURCE
        global MILK_RESOURCE

        WATER_RESOURCE -= MENU[coffee_type]['ingredients']['water']
        COFFEE_RESOURCE -= MENU[coffee_type]['ingredients']['coffee']

        if coffee_type == "espresso":
            MILK_RESOURCE = 0
        else:
            MILK_RESOURCE -= MENU[coffee_type]['ingredients']['milk']

        resources.update({
            "water": WATER_RESOURCE,
            "milk": MILK_RESOURCE,
            "coffee": COFFEE_RESOURCE
        })

        return resources

    order = input("What would you like? (espresso/latte/cappuccino)")

    if order == "espresso" or order == "latte" or order == "cappuccino":
        prepare_order(order)

    elif order == "report":
        is_coffee = False
        print_report()

    elif order == "off":
        is_coffee = False

    def print_report():
        for resource in resources:
            print(f"{resource}: {resources[resource]}")
        print(f"Money: {profit}")











