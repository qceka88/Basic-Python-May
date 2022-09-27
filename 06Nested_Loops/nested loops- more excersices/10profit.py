money_1lv = int(input())
money_2lv = int(input())
money_5lv = int(input())
needed_sum = int(input())

for leva01 in range(money_1lv + 1):
    for leva02 in range(money_2lv + 1):
        for leva05 in range(money_5lv + 1):
            if ((leva01 * 1) + (leva02 * 2) + (leva05 * 5)) == needed_sum:
                print(f"{leva01} * 1 lv. + {leva02} * 2 lv. + {leva05} * 5 lv. = {needed_sum} lv.")
