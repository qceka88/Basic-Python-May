drink = input()
sweetness = input()
qty_drinks = int(input())

price = 0

if drink == "Espresso":
    if sweetness == "Without":
        price = 0.9 * 0.65
    elif sweetness == "Normal":
        price = 1
    elif sweetness == "Extra":
        price = 1.20
elif drink == "Cappuccino":
    if sweetness == "Without":
        price = 1 * 0.65
    elif sweetness == "Normal":
        price = 1.20
    elif sweetness == "Extra":
        price = 1.60
elif drink == "Tea":
    if sweetness == "Without":
        price = 0.5 * 0.65
    elif sweetness == "Normal":
        price = 0.6
    elif sweetness == "Extra":
        price = 0.7

total_price = price * qty_drinks


if drink == "Espresso" and qty_drinks > 5:
    total_price = total_price * 0.75
if total_price > 15 :
    total_price = total_price * 0.8

print(f"You bought {qty_drinks} cups of {drink} for {total_price:.2f} lv.")
