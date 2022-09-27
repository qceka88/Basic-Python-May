type_flowers = input()
count_flower = int(input())
budget = int(input())

sum = 0
if type_flowers == "Roses":
    sum = 5 * count_flower
    if count_flower > 80:
        sum = sum * 0.90
elif type_flowers == "Dahlias":
    sum = 3.80 * count_flower
    if count_flower > 0.90:
        sum = sum * 0.85
elif type_flowers == "Tulips":
    sum = 2.80 * count_flower
    if count_flower > 80:
        sum = sum * 0.85
elif type_flowers == "Narcissus":
    sum = 3 * count_flower
    if count_flower < 120:
        sum = sum * 1.15
elif type_flowers == "Gladiolus":
    sum = 2.5 * count_flower
    if count_flower < 80:
        sum = sum * 1.20
difference = abs(budget - sum)

if sum <= budget:
    print(f"Hey, you have a great garden with {count_flower} {type_flowers} and {difference:.2f} leva left.")

else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
