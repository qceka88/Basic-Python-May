from math import ceil

heith = int(input())
width = int(input())
windows_doors = int(input())
command = input()

area = heith * width * 4
total_area = area - (area * windows_doors / 100)
paint_total = 0

is_tired = False
enough_paint = False
left_paint = False

while command != "Tired!":
    paint = int(command)
    paint_total += paint

    if total_area == paint_total:
        enough_paint = True
        break
    if total_area < paint_total:
        left_paint = True
        break
    command = input()
    if command == "Tired!":
        is_tired = True
        break

diff = abs(total_area - paint_total)

if enough_paint:
    print("All walls are painted! Great job, Pesho!")
if is_tired:
    print(f"{ceil(diff)} quadratic m left.")
if left_paint:
    print(f"All walls are painted and you have {int(diff)} l paint left!")
