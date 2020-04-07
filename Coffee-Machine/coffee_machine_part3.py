water = int(input("Write how many ml of water the coffee machine has: "))
milk = int(input("Write how many ml of milk the coffee machine has: "))
beans = int(input("Write how many grams of coffee beans the coffee machine has: "))
drinks = int(input("Write how many cups of coffee you will need: "))
max_cups = min(water // 200, milk // 50, beans // 15)
if drinks < max_cups:
    print("Yes, I can make that amount of coffee (and even "
          + str(max_cups - drinks)
          + " more than that)")
elif water - (drinks * 200) >= 0 \
        and milk - (drinks * 50) >= 0 \
        and beans - (drinks * 15) >= 0:
    print("Yes, I can make that amount of coffee.")
else:
    print("No, I can make only " 
          + str(min(water // 200, milk // 50, beans // 15))
          + " cups of coffee.")
