cakesQty = int(input())

bestBaker = 0
bestName = ""
currentBest = 0
currentName = ""
for i in range(1, cakesQty + 1):
    bakerName = input()
    command = input()
    currentPoints = 0

    while command != "Stop":
        inputPoints = int(command)
        currentPoints += inputPoints
        command = input()
    print(f"{bakerName} has {currentPoints} points.")
    if currentPoints > currentBest:
        currentBest = currentPoints
        currentName = bakerName
        print(f"{currentName} is the new number 1!")
    if currentBest > bestBaker:
        bestBaker = currentBest
        bestName = currentName
print(f"{bestName} won competition with {bestBaker} points!")