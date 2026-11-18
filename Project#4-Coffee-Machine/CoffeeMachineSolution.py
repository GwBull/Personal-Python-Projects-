# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# TODO: Print report.
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
## create all the dictionaries and variables needed to run the coffee machine program.`

match MENU:
    case "1":
        print("Espresso")
    case "2":
        print("Latte")
    case "3":
        print("Cappuccino")
    case "report":
        print_report()
    case _:
        print("Invalid choice")

if answer == "1":
    if resources["water"] >= MENU["espresso"]["ingredients"]["water"] and resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
        print("Here is your espresso. Enjoy!")
    else:
        print("Sorry, there is not enough resources to make an espresso.")

elif answer == "2":
    print("Please inter coins cost of latte is $2.50")
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    qaurters = int(input("How many quarters?: "))
    pennies = int(input("How many pennies?: "))

    pennies = pennies * 0.01
    nickels = nickels * 0.05
    dimes = dimes * 0.10
    qaurters = qaurters * 0.25

    total = pennies + nickels + dimes + qaurters

    if total < MENU["latte"]["cost"]:
        print("Sorry, that's not enough money. Money refunded.")

    change = calculate_change(total, MENU["latte"]["cost"])
    if change > 0:
        print(f"Here is your change: ${change:.2f}")

    if resources["water"] >= MENU["latte"]["ingredients"]["water"] and resources["milk"] >= MENU["latte"]["ingredients"]["milk"] and resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
        resources["water"] -= MENU["latte"]["ingredients"]["water"]
        resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
        print("Here is your latte. Enjoy!")
    else:
        print("Sorry, there is not enough resources to make a latte.")

elif answer == "3":
    if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"] and resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"] and resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]:
        resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
        print("Here is your cappuccino. Enjoy!")
    else:
        print("Sorry, there is not enough resources to make a cappuccino.")

## start of the function to print the report of the resources available in the coffee machine.
def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
## create a function to calculate the change to be returned to the user after they have paid for their coffee.
def calculate_change(total, cost):
    change = total - cost
    return change
def
