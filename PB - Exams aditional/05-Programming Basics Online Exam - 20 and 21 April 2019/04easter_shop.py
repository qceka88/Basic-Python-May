initialEggs = int(input())
command = input()

notEnoughEggs = False
soldEggs = 0
while command != "Close":
    action = command
    eggsQty = int(input())

    if action == "Fill":
        initialEggs += eggsQty
    if action == "Buy":
        if (initialEggs - eggsQty) < 0:
            notEnoughEggs = True
            break
        initialEggs -= eggsQty
        soldEggs += eggsQty
    command = input()

if notEnoughEggs:
    print("Not enough eggs in store!")
    print(f"You can buy only {initialEggs}.")
else:
    print("Store is closed!")
    print(f"{soldEggs} eggs sold.")
