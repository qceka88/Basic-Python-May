town = input()
type = input()
card = input()
days = int(input())

price = 0
invalid_type = False

if town == "Bansko" or town == "Borovets":
    if type == "withEquipment":
        price = 100
        if card == "yes":
            price = price * 0.90
    elif type == "noEquipment":
        price = 80
        if card == "yes":
            price = price * 0.95
    else:
        invalid_type = True
elif town == "Varna" or town == "Burgas":
    if type == "withBreakfast":
        price = 130
        if card == "yes":
            price *= 0.88
    elif type == "noBreakfast":
        price = 100
        if card == "yes":
            price *= 0.93
    else:
        invalid_type = True
else:
    invalid_type = True

total_price = price * days
if invalid_type:
    print("Invalid input!")
else:
    if days < 1:
        print("Days must be positive number!")
    elif days > 7:
        total_price -= price
        print(f"The price is {total_price:.2f}lv! Have a nice time!")
    else:
        print(f"The price is {total_price:.2f}lv! Have a nice time!")
