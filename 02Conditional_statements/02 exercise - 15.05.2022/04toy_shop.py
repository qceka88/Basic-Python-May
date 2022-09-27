trip_price = float(input())
puzzle_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())
total_sum = puzzle_count * 2.6 + dolls_count * 3 + bears_count * 4.1 + minions_count * 8.2 + trucks_count * 2
total_toys = puzzle_count + dolls_count + bears_count + minions_count + trucks_count
if total_toys >= 50:
    total_sum = total_sum * 0.75

total_sum = total_sum - total_sum * 0.1
difference = abs(total_sum - trip_price)
if total_sum >= trip_price:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")
