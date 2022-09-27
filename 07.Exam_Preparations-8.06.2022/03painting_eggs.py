size_eggs = input()
color_eggs = input()
number_partides = int(input())
total_eggs = 0
one_batch_price = 0

if size_eggs == "Large":
    if color_eggs == "Red":
        one_batch_price = 16
    elif color_eggs == "Green":
        one_batch_price = 12
    elif color_eggs == "Yellow":
        one_batch_price = 9
elif size_eggs == "Medium":
    if color_eggs == "Red":
        one_batch_price = 13
    elif color_eggs == "Green":
        one_batch_price = 9
    elif color_eggs == "Yellow":
        one_batch_price = 7
elif size_eggs == "Small":
    if color_eggs == "Red":
        one_batch_price = 9
    elif color_eggs == "Green":
        one_batch_price = 8
    elif color_eggs == "Yellow":
        one_batch_price = 5

total_sum = number_partides * one_batch_price
total_sum *= 0.65

print(f"{total_sum:.2f} leva.")

