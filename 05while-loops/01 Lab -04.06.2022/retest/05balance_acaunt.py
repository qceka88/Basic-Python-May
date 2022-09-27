total_money = 0
command = input()

while command != "NoMoreMoney":
    money = float(command)
    if money < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {money:.2f}")
    total_money += money
    command = input()

print(f"Total: {total_money:.2f}")
