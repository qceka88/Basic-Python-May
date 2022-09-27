degree = int(input())
part_of_day = input()
outfit = ""
shoes = ""
if part_of_day == "Morning":
    if 10 <= degree <= 18:
        outfit="Sweatshirt"
        shoes="Sneakers"
    elif 18 < degree <= 24:
        outfit="Shirt"
        shoes="Moccasins"
    else:
        outfit="T-Shirt"
        shoes="Sandals"
elif part_of_day == "Afternoon":
    if 10 <= degree <= 18:
        outfit="Shirt"
        shoes="Moccasins"
    elif 18 < degree <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
    else:
        outfit="Swim Suit"
        shoes="Barefoot"
elif part_of_day == "Evening":
        outfit="Shirt"
        shoes="Moccasins"


print(f"It's {degree} degrees, get your {outfit} and {shoes}.")
