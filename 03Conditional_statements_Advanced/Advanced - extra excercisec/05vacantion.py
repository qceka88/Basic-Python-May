budget = float(input())
season = input()

place = ""
loaction = ""
price = 0

if season == "Summer":
    location = "Alaska"
elif season == "Winter":
    location = "Morocco"

if budget <= 1000:
    place = "Camp"
    if season == "Summer":
        price = budget * 0.65
    elif season == "Winter":
        price = budget * 0.45
elif budget <= 3000:
    place = "Hut"
    if season == "Summer":
        price = budget * 0.80
    elif season == "Winter":
        price = budget * 0.60
else:
    place = "Hotel"
    price = budget * 0.9

print(f"{location} - {place} - {price:.2f}")
