needed_profit = float(input())

command = input()
total_price = 0
price = 0
sum_reached = False
party = False
while command != "Party!":
    price = int(len(command))
    coctails_qty = int(input())
    purchase = price * coctails_qty
    if purchase % 2 != 0:
        total_price += (price * 0.75) * coctails_qty
    else:
        total_price += price * coctails_qty
    if total_price >= needed_profit:
        sum_reached = True
        break
    command = input()
    if command == "Party!":
        party = True
        break

diff = needed_profit - total_price
if sum_reached:
    print("Target acquired.")
    print(f"Club income - {total_price:.2f} leva.")
if party:
    print(f"We need {diff:.2f} leva more.")
    print(f"Club income - {total_price:.2f} leva.")
