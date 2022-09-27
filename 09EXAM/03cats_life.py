from math import floor

cat_breed = input()
sex_of_cat = input()

moths = 0
wrong_breed=False

if sex_of_cat == "f":
    if cat_breed == "British Shorthair":
        moths = 14 * 12 / 6
    elif cat_breed == "Siamese":
        moths = 16 * 12 / 6
    elif cat_breed == "Persian":
        moths = 15 * 12 / 6
    elif cat_breed == "Ragdoll":
        moths = 17 * 12 / 6
    elif cat_breed == "American Shorthair":
        moths = 13 * 12 / 6
    elif cat_breed == "Siberian":
        moths = 12 * 12 / 6
    else:
        wrong_breed = True

elif sex_of_cat == "m":
    if cat_breed == "British Shorthair":
        moths = 13 * 12 / 6
    elif cat_breed == "Siamese":
        moths = 15 * 12 / 6
    elif cat_breed == "Persian":
        moths = 14 * 12 / 6
    elif cat_breed == "Ragdoll":
        moths = 16 * 12 / 6
    elif cat_breed == "American Shorthair":
        moths = 12 * 12 / 6
    elif cat_breed == "Siberian":
        moths = 11 * 12 / 6
    else:
        wrong_breed=True

if wrong_breed:
   print(f"{cat_breed} is invalid cat!")
else:
    print(f"{floor(moths)} cat months")
