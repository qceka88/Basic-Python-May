budget = float(input())
season = input()

price = 0
car = ""
clas = ""
if budget <= 100:
    clas = "Economy class"
    if season == "Summer":
        price = budget * 0.35
        car = "Cabrio"
    elif season == "Winter":
        price = budget * 0.65
        car = "Jeep"
elif budget <= 500:
    clas = "Compact class"
    if season == "Summer":
        price = budget * 0.45
        car = "Cabrio"
    elif season == "Winter":
        price = budget * 0.80
        car = "Jeep"
else:
    clas="Luxury class"
    car="Jeep"
    price= budget* 0.9

print(f"{clas}")
print(f"{car} - {price:.2f}")
