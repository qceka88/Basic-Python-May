needed_money = float(input())
init_money = float(input())

count_spend = 0
all_days_count = 0
while init_money < needed_money:
    if count_spend == 5:
        break

    action = input()
    amoutn = float(input())
    all_days_count += 1

    if action == "spend":
        count_spend += 1
        init_money -= amoutn
        if init_money < 0:
            init_money = 0
    elif action == "save":
        count_spend = 0
        init_money += amoutn

if count_spend == 5:
    print("You can't save the money.")
    print(all_days_count)
else:
    print(f"You saved the money for {all_days_count} days.")
