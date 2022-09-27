start = int(input())
final = int(input())
magic_number = int(input())

founded_combination = False
count_combinations = 0

for first_number in range(start, final + 1):
    for second_number in range(start, final + 1):
        count_combinations += 1
        if first_number + second_number == magic_number:
            founded_combination=True
            break
    if founded_combination:
        break

if founded_combination:
    print(f"Combination N:{count_combinations} ({first_number} + {second_number} = {magic_number})")
else:
    print(f"{count_combinations} combinations - neither equals {magic_number}")
