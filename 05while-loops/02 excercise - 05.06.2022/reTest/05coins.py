coins_input = float(input())
chagne_coins = round(coins_input * 100)
coins = 0
while chagne_coins != 0:
    if chagne_coins >= 200:
        chagne_coins -= 200
        coins += 1
    elif chagne_coins >= 100:
        chagne_coins -= 100
        coins += 1
    elif chagne_coins >= 50:
        chagne_coins -= 50
        coins += 1
    elif chagne_coins >= 20:
        chagne_coins -= 20
        coins += 1
    elif chagne_coins >= 10:
        chagne_coins -= 10
        coins += 1
    elif chagne_coins >= 5:
        chagne_coins -= 5
        coins += 1
    elif chagne_coins >= 2:
        chagne_coins -= 2
        coins += 1
    elif chagne_coins >= 1:
        chagne_coins -= 1
        coins += 1

print(coins)