budget = float(input())
command = input()

counter = 0
stopComand = False
totalBill = 0
while command != "Stop":
    productPrice = float(input())
    counter += 1
    if counter % 3 == 0:
        totalBill += productPrice/2
    else:
        totalBill += productPrice

    if budget < totalBill:
        needMoney = abs(budget - totalBill)
        print("You don't have enough money!")
        print(f"You need {needMoney:.2f} leva!")
        break
    command = input()
    if command == "Stop":
        stopComand = True
        break

if stopComand:
    print(f"You bought {counter} products for {totalBill:.2f} leva.")
