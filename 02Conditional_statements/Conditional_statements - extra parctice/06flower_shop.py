from math import floor, ceil

magnolias_count = int(input())
magenta_flower_count = int(input())
roses_count = int(input())
cactus_count = int(input())
gift_price = float(input())

flowers_total_price = 3.25 * magnolias_count + 4 * magenta_flower_count + 3.5 * roses_count + 8 * cactus_count
profit = flowers_total_price * 0.95
balance = abs(profit - gift_price)
if profit < gift_price:
    print(f"She will have to borrow {ceil(balance)} leva.")
else:
    print(f"She is left with {floor(balance)} leva.")
