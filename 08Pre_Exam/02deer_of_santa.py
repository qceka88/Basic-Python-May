from math import floor,ceil

days = int(input())
food = int(input())
first_deer_eat = float(input())
second_deer_eat = float(input())
third_deer_eat = float(input())

total_deer_eat = (first_deer_eat + second_deer_eat + third_deer_eat) * days

diff = abs(food - total_deer_eat)

if total_deer_eat < food:
    print(f"{floor(diff)} kilos of food left.")
else:
    print(f"{ceil(diff)} more kilos of food are needed.")

