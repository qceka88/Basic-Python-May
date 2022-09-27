count_of_numbers = int(input())
left_sum = 0
right_sum = 0
for numbers in range(2 * count_of_numbers):
    curent_number=int(input())
    if numbers < count_of_numbers:
        left_sum += curent_number
    else:
        right_sum += curent_number
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(left_sum - right_sum)
    print(f"No, diff = {diff}")