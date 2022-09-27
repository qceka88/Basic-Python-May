from math import floor,ceil

days_off=int(input())
food_total_kg=int(input())
dog_eat_kg=float(input())
cat_eat_kg=float(input())
turtle_eat_g=float(input())

eat_per_day = dog_eat_kg+cat_eat_kg+(turtle_eat_g/1000)
eat_total = eat_per_day * days_off
difference=abs(eat_total-food_total_kg)

if eat_total <= food_total_kg:
    print(f"{floor(difference)} kilos of food left.")
else:
    print(f"{ceil(difference)} more kilos of food are needed.")