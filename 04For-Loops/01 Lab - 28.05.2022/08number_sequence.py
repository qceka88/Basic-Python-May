
count_of_numbers = int(input())
current_number=int(input())
max_numder = current_number
min_numder = current_number
for numbers in range(count_of_numbers-1):
    current_number = int(input())
    if current_number > max_numder:
        max_numder = current_number
    if current_number < min_numder:
        min_numder = current_number
print(f"Max number: {max_numder}")
print(f"Min number: {min_numder}")
