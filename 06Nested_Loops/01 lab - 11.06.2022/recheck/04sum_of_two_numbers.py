first_number = int(input())
second_number = int(input())
magic_number = int(input())

founded=False
count_combinations = 0
for first in range(first_number, second_number + 1):
    for second in range(first_number, second_number + 1):
        count_combinations += 1
        if first + second == magic_number:
            founded = True
            break
    if founded:
        break

if founded:
    print(f"Combination N:{count_combinations} ({first} + {second} = {magic_number})")
else:
    print(f"{count_combinations} combinations - neither equals {magic_number}")

