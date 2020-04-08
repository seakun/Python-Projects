water = 400
milk = 540
beans = 120
cups = 9
money = 550

action = input("Write action (buy, fill, take, remaining, exit): ")

while action != "exit":
    if action == "remaining":
        print("The coffee machine has: ")
        print(str(water) + " of water")
        print(str(milk) + " of milk")
        print(str(beans) + " of coffee beans")
        print(str(cups) + " of disposable cups")
        print(str(money) + " of money")
    elif action == "fill":
        add_water = int(input("Write how many ml of water do you want to add:"))
        water += add_water
        add_milk = int(input("Write how many ml of milk do you want to add:"))
        milk += add_milk
        add_beans = int(input("Write how many grams of coffee beans do you want to add:"))
        beans += add_beans
        add_cups = int(input("Write how many disposable cups of coffee do you want to add:"))
        cups += add_cups
    elif action == "take":
        print("I gave you " + str(money))
        money -= money
    else:
        while True:
            options = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            if options == "1":
                if min(water - 250, beans - 16, cups - 1) < 0:
                    if water - 250 < 0:
                        print("Sorry, not enough " + str(water) + "!")
                    elif beans - 16 < 0:
                        print("Sorry, not enough " + str(beans) + "!")
                    else:
                        print("Sorry, not enough " + str(cups) + "!")
                else:
                    print("I have enough resources, making you a coffee!")
                    water -= 250
                    beans -= 16
                    cups -= 1
                    money += 4
            elif options == "2":
                if min(water - 350, milk - 75, beans - 16, cups - 1) < 0:
                    if water - 350 < 0:
                        print("Sorry, not enough " + str(water) + "!")
                    elif milk - 75 < 0:
                        print("Sorry, not enough " + str(milk) + "!")
                    elif beans - 20 < 0:
                        print("Sorry, not enough " + str(beans) + "!")
                    else:
                        print("Sorry, not enough " + str(cups) + "!")
                else:
                    print("I have enough resources, making you a coffee!")
                    water -= 350
                    milk -= 75
                    beans -= 20
                    cups -= 1
                    money += 7
            elif options == "3":
                if min(water - 200, milk - 100, beans - 12, cups - 1) < 0:
                    if water - 200 < 0:
                        print("Sorry, not enough " + str(water) + "!")
                    elif milk - 100 < 0:
                        print("Sorry, not enough " + str(milk) + "!")
                    elif beans - 12 < 0:
                        print("Sorry, not enough " + str(beans) + "!")
                    else:
                        print("Sorry, not enough " + str(cups) + "!")
                else:
                    print("I have enough resources, making you a coffee!")
                    water -= 200
                    milk -= 100
                    beans -= 12
                    cups -= 1
                    money += 6
            else:
                break

    action = input("Write action (buy, fill, take, remaining, exit): ")
