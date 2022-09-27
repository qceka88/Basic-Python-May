budget = float(input())
command = input()

payment = 0


while command != "ACITON":
    actorName = command
    nameLen = len(actorName)

    if nameLen <= 15:
        paymеnt = float(input())
        budget -= paymеnt
    else:
        paymеnt = budget * 0.2
        budget -= paymеnt
    command=input()
    if command == "ACTION":
        break
    if budget < 0:
        break

if budget >=0:
    print(f"We are left with {abs(budget):.2f} leva.")
else:
    print(f"We need {abs(budget):.2f} leva for our actors.")
