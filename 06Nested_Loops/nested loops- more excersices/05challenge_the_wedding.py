man_qty = int(input())
women_qty = int(input())
max_table = int(input())

counter_table = 0

for man in range(1, man_qty + 1):
    for women in range(1, women_qty + 1):
        if counter_table < max_table:
           print(f"({man} <-> {women})", end=" ")
           counter_table += 1

