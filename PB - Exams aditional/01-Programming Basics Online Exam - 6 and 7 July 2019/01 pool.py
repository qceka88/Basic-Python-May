from math import ceil

people_qty = int(input())
enter_tax = float(input())
chair_tax = float(input())
umbrella_tax = float(input())

want_chair=ceil(people_qty*0.75)
want_umbrella=ceil(people_qty/2)

total_chair_tax = want_chair * chair_tax
total_umbrella_tax = want_umbrella * umbrella_tax
total_enter_tax = people_qty * enter_tax
extras_tax = total_chair_tax + total_umbrella_tax

total_cost = total_enter_tax + extras_tax

print(f"{total_cost:.2f} lv.")
