def show_state_machine():
    print("The coffee machine has:")
    print(water, " of water")
    print(milk, " of milk")
    print(coffee_beans, " of coffee beans")
    print(disposable_cups, " of disposable cups")
    print("$", money, " of money")


def verify_resources(water_desc, milk_desc, coffee_beans_desc, disposable_cups_desc, money_desc):
    global water, milk, coffee_beans, disposable_cups, money
    if water < water_desc:
        return "Sorry,not enough water!"
    elif milk < milk_desc:
        return "Sorry,not enough milk!"
    elif coffee_beans < coffee_beans_desc:
        return "Sorry,not enough coffee beans!"
    elif disposable_cups < disposable_cups_desc:
        return "Sorry,not enough disposable cups!"
    elif money < money_desc:
        return "Sorry,not enough money!"
    else:
        return ""


def manage_resources(water_desc, milk_desc, coffee_beans_desc, disposable_cups_desc, money_desc):
    global water, milk, coffee_beans, disposable_cups, money
    water += water_desc
    milk += milk_desc
    coffee_beans += coffee_beans_desc
    disposable_cups += disposable_cups_desc
    money += money_desc


def buy():
    while True:
        choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if choice == "1":
            if verify_resources(250, 0, 16, 1, -4) != "":
                print(verify_resources(250, 0, 16, 1, -4))
                break
            else:
                print("I have enough resources, making you a coffee!")
                manage_resources(-250, 0, -16, -1, 4)
                break
        elif choice == "2":
            if verify_resources(250, 0, 16, 1, -4) != "":
                print(verify_resources(250, 0, 16, 1, -4))
                break
            else:
                print("I have enough resources, making you a coffee!")
                manage_resources(-350, -75, -20, -1, 7)
                break
        elif choice == "3":
            if verify_resources(250, 0, 16, 1, -4) != "":
                print(verify_resources(250, 0, 16, 1, -4))
                break
            else:
                print("I have enough resources, making you a coffee!")
                manage_resources(-200, -100, -12, -1, 6)
                break
        elif choice == "back":
            break


def fill():
    water_added = int(input("Write how many ml of water do you want to add: "))
    milk_added = int(input("Write how many ml of milk do you want to add: "))
    coffee_beans_added = int(input("Write how many grams of coffee beans do you want to add: "))
    disposable_cups_added = int(input("Write how many disposable cups of coffee do you want to add: "))
    manage_resources(water_added, milk_added, coffee_beans_added, disposable_cups_added, 0)


def take():
    print("I gave you $", money)
    manage_resources(0, 0, 0, 0, -money)


def select():
    while True:
        choice = str(input("Write action (buy, fill, take, remaining, exit): "))
        if choice == "buy":
            buy()
        elif choice == "fill":
            fill()
        elif choice == "take":
            take()
        elif choice == "remaining":
            show_state_machine()
        elif choice == "exit":
            break


water = 400
milk = 540
coffee_beans = 120
disposable_cups = 9
money = 550
select()
