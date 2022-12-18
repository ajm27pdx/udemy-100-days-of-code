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
    "water": 3000,
    "milk": 0,
    "coffee": 10000,
    "money": 0,
}


def print_report():
    # TODO: Add units
    print("Current Resources:")
    print(f"Water: {resources['water']}ml\n" +
          f"Milk: {resources['milk']}ml\n" +
          f"Coffee: {resources['coffee']}g\n" +
          f"Money: ${resources['money']:0.2f}\n")


def order(item):
    match check_supplies(item):
        case 'water':
            print("water")
        case 'milk':
            print("milk")
        case 'coffee':
            print("coffee")
        case 'pass':
            if accept_payment(item):
                reduce_resources(item)
                print(f"Enjoy your {item.capitalize()}")


def check_supplies(item):
    i = 0
    for resource in resources:
        if resource in MENU[item]['ingredients']:
            if resources[resource] < MENU[item]['ingredients'][resource]:
                return resource
    return 'pass'


def accept_payment(item):
    print(f"The cost of your {item} is ${MENU[item]['cost']:.2f}")
    q = int(input("Enter Quarters: "))
    d = int(input("Enter Dimes: "))
    n = int(input("Enter Nickels: "))
    p = int(input("Enter Pennies: "))

    total = q * 0.25 + d * 0.1 + n * 0.05 + p * 0.01
    print(f'You entered ${total:0.2f}')

    if total >= MENU[item]['cost']:
        print(f"Your change is ${total - MENU[item]['cost']:0.2f}")
        return True
    else:
        print(f"Sorry that's not enough money. Money refunded.")
        return False


def reduce_resources(item):
    for resource in resources:
        if resource in MENU[item]['ingredients']:
            resources[resource] -= MENU[item]['ingredients'][resource]

    resources['money'] += MENU[item]['cost']


running = True

while running:
    print("Welcome to CoffeeHub, where the cream is free!")
    choice = input("What would you like? ").lower()

    if choice == "off":
        print("Thannnkk Yyyyyo...")
        running = False
    elif choice == "report":
        print_report()
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        order(choice)
    else:
        print("Invalid Input")


