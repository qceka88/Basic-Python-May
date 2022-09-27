distance = int(input())
tariff = input()
taxi_day_tax = 0.79
taxi_night_tax = 0.9
autobus = 0.09
train = 0.06
first_tax = 0.7

if distance < 20:
    if tariff == "day":
        price = distance * taxi_day_tax + first_tax
        print(f"{price:.2f}")
    else:
        price = distance * taxi_night_tax + first_tax
        print(f"{price:.2f}")
elif distance < 100:
    price = autobus * distance
    print(f"{price:.2f}")
else:
    price = distance * train
    print(f"{price:.2f}")
