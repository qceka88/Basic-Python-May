needed_money = float(input())
init_money = float(input())

days_spend = 0
total_days = 0

while init_money < needed_money:
    if days_spend == 5:
        break

    action = input()
    input_money = float(input())
    total_days += 1

    if action == "spend":
        days_spend += 1
        init_money -= input_money
        if init_money < 0:
            init_money = 0
    elif action == "save":
        days_spend = 0
        init_money += input_money

if days_spend == 5:
    print("You can't save the money.")
    print(days_spend)
else:
    print(f"You saved the money for {total_days} days.")
