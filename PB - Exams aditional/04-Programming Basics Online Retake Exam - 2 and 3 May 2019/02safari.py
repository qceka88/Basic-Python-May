budget = float(input())
neededFuel = float(input())
dayOfWeek = input()

fuelPrice = neededFuel * 2.1
totalPrice = fuelPrice + 100

if dayOfWeek == "Saturday":
    totalPrice *= 0.9
elif dayOfWeek == "Sunday":
    totalPrice *= 0.8
else:
    totalPrice = totalPrice
diff = abs(budget - totalPrice)
if budget >= totalPrice:
    print(f"Safari time! Money left: {diff:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {diff:.2f} lv.")
