moves = int(input())

count10 = 0
count20 = 0
count30 = 0
count40 = 0
count50 = 0
count_invalid = 0
points = 0

for i in range(1, moves + 1):
    number = int(input())
    if number == 0:
        points = points + 0
        count10 += 1
    elif number < 0:
        points = points / 2
        count_invalid += 1
    elif number < 10:
        points = (20 / 100 * number) + points
        count10 += 1
    elif number < 20:
        points = (30 / 100 * number) + points
        count20 += 1
    elif number < 30:
        points = (40 / 100 * number) + points
        count30 += 1
    elif number < 40:
        points = 50 + points
        count40+=1
    elif number <= 50:
        points = 100 + points
        count50+=1
    else:
        points = points / 2
        count_invalid += 1

print(f"{points:.2f}")

count10_percent= count10/ moves * 100
print(f"From 0 to 9: {count10_percent:.2f}%")
count20_percent= count20/ moves * 100
print(f"From 10 to 19: {count20_percent:.2f}%")
count30_percent= count30/ moves * 100
print(f"From 20 to 29: {count30_percent:.2f}%")
count40_percent= count40/ moves * 100
print(f"From 30 to 39: {count40_percent:.2f}%")
count50_percent= count50 / moves * 100
print(f"From 40 to 50: {count50_percent:.2f}%")
count_invalid= count_invalid/ moves * 100
print(f"Invalid numbers: {count_invalid:.2f}%")