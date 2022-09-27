destination = input()

while destination != "End":
    needed_money = float(input())
    sum = 0
    while needed_money > sum:
        input_money = float(input())
        sum += input_money
    print(f"Going to {destination}!")
    destination = input()
