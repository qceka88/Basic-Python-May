budget = int(input())
season = input()
people = int(input())

price = 0
if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600

if people <=6:
    price = price * 0.90
elif  people <= 11:
    price = price * 0.85
else:
    price = price * 0.75

if people % 2 == 0:
    if season != "Autumn":
        price = price * 0.95

diference = abs(budget - price)

if budget >= price:
    print(f"Yes! You have {diference:.2f} leva left.")
else:
    print(f"Not enough money! You need {diference:.2f} leva.")
