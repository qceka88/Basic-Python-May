food_kg = int(input())
command = input()

food_g = food_kg * 1000
eaten_food = 0
while command != "Adopted":
    dayly_food = int(command)
    eaten_food += dayly_food
    command = input()

total_food = abs(eaten_food - food_g)

if eaten_food <= food_g:
    print(f"Food is enough! Leftovers: {total_food} grams.")
else:
    print(f"Food is not enough. You need {total_food} grams more.")