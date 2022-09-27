pairs = int(input())

previous_sum = 0
current_sum = 0
for i in range(1, pairs + 1):
    num01 = int(input())
    num02 = int(input())
    previous_sum = current_sum

    current_sum = num01 + num02

    if previous_sum != current_sum:
        diff = abs(previous_sum - current_sum)
    if i == 1:
        previous_sum = current_sum

if previous_sum == current_sum:
    print(f'Yes, value={current_sum}')
else:

    print(f"No, maxdiff={diff}")
