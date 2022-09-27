import sys

num = int(input())

max_num = -sys.maxsize

total_sum = 0
for i in range(1, num + 1):
    current_num = int(input())
    total_sum = total_sum + current_num
    if current_num > max_num:
        max_num = current_num

sum = total_sum - max_num
if sum == max_num:
    print("Yes")
    print(f"Sum = {sum}")
else:
    diff= abs(sum - max_num)
    print("No")
    print(f"Diff = {diff}")