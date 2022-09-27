clients = int(input())

totalPrice = 0

for i in range(1, clients + 1):
    command = input()
    currentClientBill = 0
    productCounter = 0

    while command != "Finish":
        if command == "basket":
            currentClientBill += 1.5
        elif command == "wreath":
            currentClientBill += 3.8
        elif command == "chocolate bunny":
            currentClientBill += 7
        productCounter += 1
        command = input()
    if productCounter % 2 == 0:
        currentClientBill *= 0.80
    print(f"You purchased {productCounter} items for {currentClientBill:.2f} leva.")
    totalPrice += currentClientBill

averragePrice = totalPrice / clients
print(f"Average bill per client is: {averragePrice:.2f} leva.")
