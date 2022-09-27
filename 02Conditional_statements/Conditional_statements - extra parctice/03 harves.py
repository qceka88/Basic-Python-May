from math import ceil, floor

vines_sqm = int(input())
production_sqm = float(input())
required_wine_lt = int(input())
workers = int(input())
wine = vines_sqm * production_sqm * 0.4 / 2.5
amount = abs(wine - required_wine_lt)
liters_person = amount / workers
if wine >= required_wine_lt:
    print(f"Good harvest this year! Total wine: {floor(wine)} liters.")
    print(f"{ceil(amount)} liters left -> {ceil(liters_person)} liters per person.")
else:
    print(f"It will be a tough winter! More {floor(amount)} liters wine needed.")
