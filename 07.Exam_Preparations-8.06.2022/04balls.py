number_of_bals = int(input())

total_point = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
divides_balls = 0
other_balls = 0

for balls in range(number_of_bals):
    current_ball = input()
    if current_ball == "red":
        total_point += 5
        red_balls += 1
    elif current_ball == "orange":
        total_point += 10
        orange_balls += 1
    elif current_ball == "yellow":
        total_point += 15
        yellow_balls += 1
    elif current_ball == "white":
        total_point += 20
        white_balls += 1
    elif current_ball == "black":
        total_point //= 2
        divides_balls += 1
    else:
        other_balls += 1

print(f"Total points: {total_point}")
print(f"Red balls: {red_balls}")
print(f"Orange balls: {orange_balls}")
print(f"Yellow balls: {yellow_balls}")
print(f"White balls: {white_balls}")
print(f"Other colors picked: {other_balls}")
print(f"Divides from black balls: {divides_balls}")
