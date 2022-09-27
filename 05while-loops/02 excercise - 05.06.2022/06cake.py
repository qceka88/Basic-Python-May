width = int(input())
length = int(input())

total_count_pieces = width * length

input_line = input()
no_more_pieces = False
while input_line != "STOP":
    current_pieces = int(input_line)
    total_count_pieces -= current_pieces
    if total_count_pieces <= 0:
        no_more_pieces = True
        break

    input_line = input()
if no_more_pieces:
    print(f"No more cake left! You need {abs(total_count_pieces)} pieces more.")
else:
    print(f"{total_count_pieces} pieces are left.")
