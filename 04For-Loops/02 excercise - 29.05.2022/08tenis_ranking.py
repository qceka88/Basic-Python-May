from math import floor

turnirs = int(input())
start_points = int(input())

points = 0
win_turnirs = 0

for i in range(1, turnirs + 1):
    stage = input()
    if stage == "W":
        win_turnirs += 1
        points = points + 2000
    elif stage == "F":
        points = points + 1200
    elif stage == "SF":
        points = points + 720

total_points = start_points + points
average_points = points / turnirs
sucses = win_turnirs / turnirs * 100

print(f"Final points: {total_points}")
print(f"Average points: {floor(average_points)}")
print(f"{sucses:.2f}%")
