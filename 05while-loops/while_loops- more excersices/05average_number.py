init_input = int(input())
sum = 0
counts = 0
while counts in range(init_input + 1):
    counts += 1
    current_number = int(input())
    sum += current_number
    if counts == init_input:
        break

average_number = sum / counts
print(f"{average_number:.2f}")
