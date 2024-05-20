import sys

# ask what cx wants espresso/latte/cappucino
# other comands off: ends program, report: shows all resources -
##### like water, milk, coffee, and money in machine
# start: what would you like?
##### if drink then check resorses, if True then ask for money, if enough then return any change, -
##### and say "enjoy your drink" then recall start()
# start()
##### if off sys.ext()
##### if report: print all resouces

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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(drink):
    for resource in drink:
        if drink[resource] <= resources[resource]:
            return True
        else:
            print(f"sorry we dont have enough {resource}")
            return False


def collect_coins(cost):
    total = int(input(f"drink costs {cost} how many quarters do you give?: ")) * 0.25
    total += int(input("how many dimes would you like to give?: ")) * 0.1
    total += int(input("how many nickles would you like to give?: ")) * 0.05
    total += int(input("how many pennies would you like to give?: ")) * 0.01
    print(total)
    return total


def payment_successful(total, cost):
    if total == cost:
        print("payment acepted, change not needed")
        return True
    elif total >= cost:
        change = total - cost
        print(f"payment acepted, your change is {change}")
        return True
    else:
        print(f"sorry not enough money, hes your {total}")
        return False


def brew_drink(drink, ingredients):
    for resource in ingredients:
        resources[resource] -= ingredients[resource]
    print(f"enjoy your drink!")


is_on = True

while is_on:
    choice = input("what would you like to order? ")

    match choice:
        case "off":
            is_on = False
        case "report":
            for items in resources:
                print(f"{items}: {resources[items]}")
        case "espresso" | "latte" | "cappuccino":
            drink = MENU[choice]  # easy access to drinks dict
            if check_resources(
                drink["ingredients"]
            ):  # true or false for if resources are avalible
                payment = collect_coins(
                    drink["cost"]
                )  # ask for coinage as payment and returns total
                if payment_successful(
                    payment, drink["cost"]
                ):  # decides if money is enough | if change needed
                    brew_drink(
                        drink, drink["ingredients"]
                    )  # removes needed resources and says have a good day
