eggSize = input()
colorEgg = input()
batchQty = int(input())

price = 0

if eggSize == "Large":
    if colorEgg == "Red":
        price = 16
    elif colorEgg == "Green":
        price = 12
    elif colorEgg == "Yellow":
        price = 9
elif eggSize == "Medium":
    if colorEgg == "Red":
        price = 13
    elif colorEgg == "Green":
        price = 9
    elif colorEgg == "Yellow":
        price = 7
elif eggSize == "Small":
    if colorEgg == "Red":
        price = 9
    elif colorEgg == "Green":
        price = 8
    elif colorEgg == "Yellow":
        price = 5

prductionEggPrice = price * batchQty
expences = prductionEggPrice * 0.35

profit = prductionEggPrice - expences

print(f"{profit:.2f} leva.")
