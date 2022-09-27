init_food_kg = int(input())
food_gram = init_food_kg * 1000
commad = input()
eaten_food = 0
while commad != "Adopted":
    current_food = int(commad)
    food_gram -= current_food

    commad = input()

if food_gram >= 0:
    print(f"Food is enough! Leftovers: {food_gram} grams.")
else:
    print(f"Food is not enough. You need {abs(food_gram)} grams more.")
