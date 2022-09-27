width = int(input())
length = int(input())
heigth = int(input())

total_volume = width * length * heigth
sum_boxes = 0
input_line = input()
while input_line != "Done":
    boxes = int(input_line)
    sum_boxes += boxes

    if sum_boxes >= total_volume:
        break

    input_line = input()
diff = abs(sum_boxes - total_volume)
if sum_boxes >= total_volume:
    print(f"No more free space! You need {diff} Cubic meters more.")
else:
    print(f"{diff} Cubic meters left.")
