contractTime = input()
typeContract = input()
internetADD = input()
monthToPay = int(input())

price = 0
discount = False
if contractTime == "one":
    if typeContract == "Small":
        price = 9.98
    elif typeContract == "Middle":
        price = 18.99
    elif typeContract == "Large":
        price = 25.98
    elif typeContract == "ExtraLarge":
        price = 35.99
elif contractTime == "two":
    discount = True
    if typeContract == "Small":
        price = 8.58
    elif typeContract == "Middle":
        price = 17.09
    elif typeContract == "Large":
        price = 23.59
    elif typeContract == "ExtraLarge":
        price = 31.79
if internetADD == "yes":
    if price <= 10:
        price += 5.50
    elif price <= 30:
        price += 4.35
    else:
        price += 3.85

if discount:
    price *= 0.9625
totalPrice = price * monthToPay



print(f"{totalPrice:.2f} lv.")
