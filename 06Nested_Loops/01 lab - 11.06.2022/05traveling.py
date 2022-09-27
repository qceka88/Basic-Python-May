destination = input()

while destination != "End":
    needed_money = float(input())
    sum_money = 0
    while sum_money < needed_money:
        input_money = float(input())
        sum_money += input_money
    print(f"Going to {destination}!")

    destination = input()
