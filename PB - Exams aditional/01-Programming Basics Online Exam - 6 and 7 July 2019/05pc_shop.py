selled_games = int(input())

game_counter = 0
hearthstone_counter = 0
fornite_counter = 0
overwatch_counter = 0
others_counter = 0

for i in range(1, selled_games + 1):
    current_game = input()
    game_counter += 1
    if current_game == "Hearthstone":
        hearthstone_counter += 1
    elif current_game == "Fornite":
        fornite_counter += 1
    elif current_game == "Overwatch":
        overwatch_counter += 1
    else:
        others_counter += 1

hearthstone_percent = hearthstone_counter / game_counter * 100
fornite_percent = fornite_counter / game_counter * 100
overwatch_percent = overwatch_counter / game_counter * 100
other_percent = others_counter / game_counter * 100

print(f"Hearthstone - {hearthstone_percent:.2f}%")
print(f"Fornite - {fornite_percent:.2f}%")
print(f"Overwatch - {overwatch_percent:.2f}%")
print((f"Others - {other_percent:.2f}%"))

