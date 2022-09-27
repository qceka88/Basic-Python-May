budget = float(input())
season = input()
destination = ""
place=""
expenses = 0
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        expenses = budget * 0.30
        place = "Camp"
    elif season == "winter":
        expenses = budget * 0.70
        place = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        expenses = budget * 0.40
        place = "Camp"
    elif season == "winter":
        expenses = budget * 0.80
        place = "Hotel"
else:
    destination = "Europe"
    expenses = budget * 0.90
    place = "Hotel"

print(f"Somewhere in {destination}")
print(f"{place} - {expenses:.2f}")
