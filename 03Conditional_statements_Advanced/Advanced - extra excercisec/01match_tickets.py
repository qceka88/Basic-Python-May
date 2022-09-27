budget = float(input())
category = input()
people = int(input())

vip = 499.99
normal = 249.99
price = 0
if category == "VIP":
    price = vip * people
elif category == "Normal":
    price = normal * people
if 1 <= people < 5:
    transport = budget * 0.75
elif 5 <= people <= 9:
    transport = budget * 0.6
elif 10 <= people <= 24:
    transport = budget * 0.5
elif 25 <= people <= 49:
    transport = budget * 0.4
else:
    transport = budget * 0.25

price = price + transport
diff = abs(budget - price)
if budget > price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
