seriesBudget = float(input())
qtySeries = int(input())

totalPrice = 0

for series in range(1, qtySeries + 1):
    nameSeries = input()
    priceSeries = float(input())

    if nameSeries == "Thrones":
        priceSeries *= 0.50
        totalPrice += priceSeries
    elif nameSeries == "Lucifer":
        priceSeries *= 0.60
        totalPrice += priceSeries
    elif nameSeries == "Protector":
        priceSeries *= 0.70
        totalPrice += priceSeries
    elif nameSeries == "TotalDrama":
        priceSeries *= 0.80
        totalPrice += priceSeries
    elif nameSeries == "Area":
        priceSeries *= 0.90
        totalPrice += priceSeries
    else:
        totalPrice += priceSeries

diff = abs(seriesBudget - totalPrice)

if seriesBudget >= totalPrice:
    print(f"You bought all the series and left with {diff:.2f} lv.")
else:
    print(f"You need {diff:.2f} lv. more to buy the series!")
