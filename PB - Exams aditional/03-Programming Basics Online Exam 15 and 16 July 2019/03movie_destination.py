movieBudget = float(input())
destination = input()
season = input()
daysQty = int(input())

if season == "Winter":
    if destination == "Dubai":
        price = 45000
    elif destination == "Sofia":
        price = 17000
    elif destination == "London":
        price = 24000
elif season == "Summer":
    if destination == "Dubai":
        price = 40000
    elif destination == "Sofia":
        price = 12500
    elif destination == "London":
        price = 20500
totalPrice = price * daysQty
if destination == "Dubai":
    totalPrice = totalPrice * 0.7
if destination == "Sofia":
    totalPrice = totalPrice * 1.25
diff = abs(totalPrice - movieBudget)
if totalPrice <= movieBudget:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {diff:.2f} leva more!")
