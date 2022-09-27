daysQty = int(input())
hoursQty = int(input())

totalprice = 0

for i in range(1, daysQty + 1):
    daylyPrice = 0
    for j in range(1, hoursQty + 1):
        if i % 2 != 0 and j % 2 == 0:
            daylyPrice += 1.25
        elif i % 2 == 0 and j % 2 != 0:
            daylyPrice += 2.5
        else:
            daylyPrice += 1
    print(f"Day: {i} - {daylyPrice:.2f} leva")
    totalprice += daylyPrice
print(f"Total: {totalprice:.2f} leva")
