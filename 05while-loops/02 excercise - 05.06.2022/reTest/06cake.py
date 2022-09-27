lenght = int(input())
width = int(input())

pieces = lenght * width

input_line = input()
is_cake_left = False

while input_line != "STOP":
    current_pieces = int(input_line)
    pieces = pieces - current_pieces

    if pieces <= 0:
        is_cake_left = True
        break

    input_line = input()

if is_cake_left:
    print(f"No more cake left! You need {abs(pieces)} pieces more.")
else:
    print(f"{abs(pieces)} pieces are left.")
