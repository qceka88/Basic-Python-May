budget = float(input())
people = int(input())
price_clothing_one = float(input())
decor = budget * 0.1
all_clothes_price = people * price_clothing_one

if people >150:
    all_clothes_price=all_clothes_price*0.9

excpenses = decor + all_clothes_price

difference=abs(budget-excpenses)
if excpenses <= budget:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")