width = int(input())
lenght = int(input())
height = int(input())

volume = width * lenght * height

input_line = input()
volume_enought = False
while input_line != "Done":
    boxes = int(input_line)
    volume = volume - boxes
    if volume <= 0:
        volume_enought = True
        break
    input_line = input()

if volume_enought:
    print(f"No more free space! You need {abs(volume)} Cubic meters more.")
else:
    print(f"{abs(volume)} Cubic meters left.")
