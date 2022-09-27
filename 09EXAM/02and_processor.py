from math import floor, ceil

needed_cpu = int(input())
employe_qty = int(input())
work_days = int(input())

total_hours = employe_qty * work_days * 8

produced_cpu = floor(total_hours / 3)
price_cpu=abs((needed_cpu-produced_cpu)*110.10)

if needed_cpu > produced_cpu:
    print(f"Losses: -> {price_cpu:.2f} BGN")
else:
    print(f"Profit: -> {price_cpu:.2f} BGN")




