from math import ceil

cakesQty = int(input())

totalSugar = 0
totalFlour = 0
curMaxSugar = 0
curMaxFlour = 0

for i in range(1, cakesQty + 1):
    currentSugar = int(input())
    currentFlour = int(input())
    totalSugar += currentSugar
    totalFlour += currentFlour

    if currentSugar > curMaxSugar:
        curMaxSugar = currentSugar
    if currentFlour > curMaxFlour:
        curMaxFlour = currentFlour

sugarPacks = ceil(totalSugar / 950)
flourPacks = ceil(totalFlour / 750)

print(f"Sugar: {sugarPacks}")
print(f"Flour: {flourPacks}")
print(f"Max used flour is {curMaxFlour} grams, max used sugar is {curMaxSugar} grams.")
