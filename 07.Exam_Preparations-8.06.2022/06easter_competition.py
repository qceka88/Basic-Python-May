easter_cakes = int(input())
best_baker = ""
best_points = 0

for bakers in range(easter_cakes):
    personal_points = 0
    baker_name = input()
    command = input()
    while command != "Stop":
        value = int(command)
        personal_points += value
        command = input()
    print(f"{baker_name} has {personal_points} points.")
    if personal_points > best_points:
        best_points = personal_points
        best_baker = baker_name
        print(f"{baker_name} is the new number 1!")

print(f"{best_baker} won competition with {best_points} points!")