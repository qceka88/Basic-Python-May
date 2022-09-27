change = float(input())
coin_change = round(change * 100)

count_coins = 0
while coin_change > 0:
    if coin_change >= 200:
        coin_change -= 200
    elif coin_change >= 100:
        coin_change -= 100
    elif coin_change >= 50:
        coin_change -= 50
    elif coin_change >= 20:
        coin_change -= 20
    elif coin_change >= 10:
        coin_change -= 10
    elif coin_change >= 5:
        coin_change -= 5
    elif coin_change >= 2:
        coin_change -= 2
    elif coin_change >= 1:
        coin_change -= 1
    count_coins += 1

print(count_coins)
