food_in_KG = int(input())
food_in_G = food_in_KG * 1000
command = input()
while command != "Adopted":
    eatend_food_G = int(command)
    food_in_G -= eatend_food_G
    command = input()
if food_in_G < 0:
    print(f"Food is not enough. You need {abs(food_in_G)} grams more")
else:
    print(f"Food is enough! Leftovers: {food_in_G} grams.")
