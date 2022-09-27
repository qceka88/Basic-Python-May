input_number = int(input())

count_results = 0

for x1 in range(input_number + 1):
    for x2 in range(input_number + 1):
        for x3 in range(input_number + 1):
            if x1 + x2 + x3 == input_number:
                count_results += 1

print(count_results)
