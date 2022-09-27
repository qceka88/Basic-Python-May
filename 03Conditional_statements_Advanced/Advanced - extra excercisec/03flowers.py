chrysanthemum_qty = int(input())
rose_qty = int(input())
tulip_qty = int(input())
season = input()
holyday = input()

total_flowers=chrysanthemum_qty+rose_qty+tulip_qty
total_price = 0
if season == "Spring" or season == "Summer":
    chrysanthemums_price = chrysanthemum_qty * 2
    roses_price = rose_qty * 4.1
    tulips_price = tulip_qty * 2.5
    total_price = chrysanthemums_price + roses_price + tulips_price
    if holyday == "Y":
        total_price=total_price*1.15
    if season == "Spring" and tulip_qty >7:
        total_price=total_price*0.95
elif season == "Autumn" or season == "Winter":
    chrysanthemums_price = chrysanthemum_qty * 3.75
    roses_price = rose_qty * 4.5
    tulips_price = tulip_qty * 4.15
    total_price = chrysanthemums_price + roses_price + tulips_price
    if holyday == "Y":
        total_price=total_price*1.15
    if season == "Winter" and rose_qty >=10:
        total_price=total_price*0.9

if total_flowers >20:
    total_price=total_price*0.8

price=total_price+2
print(f"{price:.2f}")
