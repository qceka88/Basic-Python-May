import sys

max_num = -sys.maxsize
command = input()
while command != "Stop":
    current_num = int(command)
    if  current_num > max_num:
        max_num = current_num
    command = input()

print(max_num)
