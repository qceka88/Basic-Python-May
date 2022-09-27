import sys

min_num = sys.maxsize
command = input()
while command != "Stop":
    current_num = int(command)
    if  current_num < min_num:
        min_num = current_num
    command = input()

print(min_num)
