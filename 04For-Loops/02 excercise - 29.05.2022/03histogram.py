n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(1, n + 1):
    current_num = int(input())
    if current_num < 200:
        p1 += 1
    elif current_num < 400:
        p2 += 1
    elif current_num < 600:
        p3 += 1
    elif current_num < 800:
        p4 += 1
    else:
        p5 += 1

percent1 = p1 / n * 100
percent2 = p2 / n * 100
percent3 = p3 / n * 100
percent4 = p4 / n * 100
percent5 = p5 / n * 100

print(f"{percent1:.2f}%")
print(f"{percent2:.2f}%")
print(f"{percent3:.2f}%")
print(f"{percent4:.2f}%")
print(f"{percent5:.2f}%")
