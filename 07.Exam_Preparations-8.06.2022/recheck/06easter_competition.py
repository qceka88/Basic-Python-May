bakers_qty = int(input())
best_baker = ""
points = 0
for bakes in range(bakers_qty):
    baker_name = input()
    command = input()
    current_best_points = 0
    while command != "Stop":
        current_points = int(command)
        current_best_points += current_points
        command = input()
    print(f"{baker_name} has {current_best_points} points.")
    if current_best_points > points:
        points = current_best_points
        best_baker=baker_name
        print(f"{best_baker} is the new number 1!")
print(f"{best_baker} won competition with {points} points!")