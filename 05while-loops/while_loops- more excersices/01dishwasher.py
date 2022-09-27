input_line = input()
detergent = int(input_line)
total_detergent = detergent * 750

count_loads = 0
count_dishesh = 0
count_pots = 0
is_enough = False
while total_detergent >= 0:
    count_loads += 1
    input_line = input()
    if input_line == "End":
        is_enough = True
        break

    if count_loads % 3 != 0:
        dishes = int(input_line)
        count_dishesh += dishes
        total_detergent = total_detergent - (dishes * 5)
    else:
        pots = int(input_line)
        count_pots += pots
        total_detergent = total_detergent - (pots * 15)


if is_enough:
    print("Detergent was enough!")
    print(f"{count_dishesh} dishes and {count_pots} pots were washed.")
    print(f"Leftover detergent {total_detergent} ml.")
else:
    print(f"Not enough detergent, {abs(total_detergent)} ml. more necessary!")
