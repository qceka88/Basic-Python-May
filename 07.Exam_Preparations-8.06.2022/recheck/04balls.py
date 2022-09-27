balls_qty = int(input())

red_qty = 0
orange_qty = 0
yellow_qty = 0
white_qty = 0
black_qty = 0
other_qty = 0

points = 0

for balls in range(balls_qty):
    color = input()
    if color == "red":
        points += 5
        red_qty += 1
    elif color == "orange":
        points += 10
        orange_qty += 1
    elif color == "yellow":
        points += 15
        yellow_qty += 1
    elif color == "white":
        points += 20
        white_qty += 1
    elif color == "black":
        points //= 2
        black_qty += 1
    else:
        other_qty += 1

print(f"Total points: {points}")
print(f"Red balls: {red_qty}")
print(f"Orange balls: {orange_qty}")
print(f"Yellow balls: {yellow_qty}")
print(f"White balls: {white_qty}")
print(f"Other colors picked: {other_qty}")
print(f"Divides from black balls: {black_qty}")
