from math import ceil

guestsQty = int(input())
budget = int(input())

eggsQty = guestsQty * 2
cakesQty = guestsQty / 3
eggsPrice = eggsQty * 0.45
cakesPrice = ceil(cakesQty) * 4
totalPrice = eggsPrice + cakesPrice

diff = abs(totalPrice - budget)

if budget >= totalPrice:
    print(f"Lyubo bought {ceil(cakesQty)} Easter bread and {eggsQty} eggs.")
    print(f"He has {diff:.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {diff:.2f} lv. more.")