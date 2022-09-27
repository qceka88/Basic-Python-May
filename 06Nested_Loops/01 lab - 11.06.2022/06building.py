floors = int(input())
rooms = int(input())

letter_of_the_floor = ""

for current_floor in range(floors, 0, -1):
    for current_room in range(rooms):
        if current_floor == floors:
            letter_of_the_floor = "L"
        elif current_floor % 2 == 0:
            letter_of_the_floor = "O"
        else:
            letter_of_the_floor = "A"

        print(f"{letter_of_the_floor}{current_floor}{current_room}", end=" ")
    print()
# end= "\n"