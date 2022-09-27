floors=int(input())
rooms=int(input())

type=""

for current_floor in range (floors,0,-1):
    for current_room in range(rooms):
        if current_floor == floors:
            type="L"
        elif current_floor %2==0:
            type = "O"
        else:
            type= "A"
        print(f"{type}{current_floor}{current_room}", end=" ")
    print()