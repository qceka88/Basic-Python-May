start = int(input())
stop = int(input())
magic_number = int(input())

counter = 0
is_found = False
not_found=False
for i in range(start, stop + 1):
    for j in range(start, stop + 1):
        counter += 1
        if i + j == magic_number:
            is_found = True
            break
    if is_found:
        break

if is_found:
    print(f'Combination N:{counter} ({i} + {j} = {magic_number})')
else:
    print(f"{counter} combinations - neither equals {magic_number}")

