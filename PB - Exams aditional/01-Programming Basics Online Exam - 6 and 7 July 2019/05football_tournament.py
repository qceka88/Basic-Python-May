team = input()
games = int(input())

win_count = 0
equal_count = 0
lose_count = 0
scores = 0

for i in range(1, games + 1):
    result = input()
    if result == "W":
        win_count += 1
        scores += 3
    elif result == "D":
        equal_count += 1
        scores += 1
    elif result == "L":
        lose_count += 1

if games < 1:
     print(f"{team} hasn't played any games during this season.")
else:
   win_percent = win_count / games * 100
   print(f"{team} has won {scores} points during this season.")
   print("Total stats:")
   print(f"## W: {win_count}")
   print(f"## D: {equal_count}")
   print(f"## L: {lose_count}")
   print(f"Win rate: {win_percent:.2f}%")
