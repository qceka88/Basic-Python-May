projection = input()
filmPack = input()
ticketsQty = int(input())

if projection == "John Wick":
    if filmPack == "Drink":
        price = 12
    elif filmPack == "Popcorn":
        price = 15
    elif filmPack == "Menu":
        price = 19
elif projection == "Star Wars":
    if filmPack == "Drink":
        price = 18
    elif filmPack == "Popcorn":
        price = 25
    elif filmPack == "Menu":
        price = 30
elif projection == "Jumanji":
    if filmPack == "Drink":
        price = 9
    elif filmPack == "Popcorn":
        price = 11
    elif filmPack == "Menu":
        price = 14

totalPrice = price * ticketsQty
if projection == "Star Wars" and ticketsQty >=4:
    totalPrice = totalPrice * 0.7
elif projection == "Jumanji" and ticketsQty == 2:
    totalPrice = totalPrice * .85
print(f"Your bill is {totalPrice:.2f} leva.")
