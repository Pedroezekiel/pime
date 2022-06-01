menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 10,
        },
        "cost": 1.5,
    },
    "Latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

payment = {"money": 0}


def x():
    quarters = int(input(f"please insert coins \nHow many quarters?:"))
    quarters_total = quarters * 0.25
    dime = int(input(f"How many dime?:"))
    dime_total = dime * 0.10
    penny = int(input(f"How many penny?:"))
    penny_total = penny * 0.01
    nickel = int(input(f"How many dime?:"))
    nickel_total = nickel * 0.05
    total = quarters_total + dime_total + penny_total + nickel_total
    return total


def checking(o):
    if resources["water"] < menu.get(o).get("ingredients").get("water"):
        print("there is not enough water")
    elif resources["milk"] < menu.get(o).get("ingredients").get("milk"):
        print("there is not enough milk")
    elif resources["coffee"] < menu.get(o).get("ingredients").get("coffee"):
        print("there is not enough water")
    else:
        payment["money"] = payment["money"] + x() - menu.get(o).get("cost")
        resources["water"] = resources.get("water") - menu.get(o).get("ingredients").get("water")
        resources["coffee"] = resources.get("coffee") - menu.get(o).get("ingredients").get("coffee")
        resources["milk"] = resources.get("milk") - menu.get(o).get("ingredients").get("milk")
        print(f"Here is ${payment['money']} in change \nHere is your {o} Enjoy!")


while True:
    userInput = input("What would like ?(espresso/latte/cappuccino): ")
    if userInput == "STOP".lower():
        break
    elif userInput == "report":
        for i, y in resources.items():
            if i == "coffee":
                print(f"{i}:  {y}g")
            else:
                print(f"{i}:  {y}ml")
        print(f"money:  ${payment['money']}")
    elif userInput == "latte":
        checking("Latte")
    elif userInput == "cappuccino":
        checking("cappuccino")
    elif userInput == "espresso":
        if resources["water"] < menu.get("espresso").get("ingredients").get("water"):
            print("there is not enough water")
        elif resources["coffee"] < menu.get("espresso").get("ingredients").get("coffee"):
            print("there is not enough water")
        else:
            payment["money"] = + x() - menu.get("espresso").get("cost")
            resources["water"] = resources.get("water") - menu.get("espresso").get("ingredients").get("water")
            resources["coffee"] = resources.get("coffee") - menu.get("espresso").get("ingredients").get("coffee")
