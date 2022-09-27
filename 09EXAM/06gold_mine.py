loaction_qty = int(input())

for i in range(1, loaction_qty + 1):
    needed_gold = float(input())
    days = int(input())
    total_gold = 0
    for l in range(1, days + 1):
        diged_gold = float(input())
        total_gold += diged_gold
    averrage_gold = total_gold / days
    if averrage_gold>=needed_gold:
        print(f"Good job! Average gold per day: {averrage_gold:.2f}.")
    else:
        diff=abs(needed_gold-averrage_gold)
        print(f"You need {diff:.2f} gold.")
