water = 1200
milk = 540
beans = 120
cups = 9
money = 550


def print_state():
    print("The coffee machine has: ")
    print(str(water) + " of water")
    print(str(milk) + " of milk")
    print(str(beans) + " of coffee beans")
    print(str(cups) + " of disposable cups")
    print(str(money) + " of money")


print_state()

action = input("Write action (buy, fill, take): ")

if action == "fill":
    add_water = int(input("Write how many ml of water do you want to add:"))
    water += add_water
    add_milk = int(input("Write how many ml of milk do you want to add:"))
    milk += add_milk
    add_beans = int(input("Write how many grams of coffee beans do you want to add:"))
    beans += add_beans
    add_cups = int(input("Write how many disposable cups of coffee do you want to add:"))
    cups += add_cups
    print_state()
elif action == "take":
    print("I gave you " + str(money))
    money -= money
    print_state()
else:
    options = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:"))
    if options == 1:
        water -= 250
        beans -= 16
        cups -= 1
        money += 4
    elif options == 2:
        water -= 350
        milk -= 75
        beans -= 20
        cups -= 1
        money += 7
    else:
        water -= 200
        milk -= 100
        beans -= 12
        cups -= 1
        money += 6
    print_state()
