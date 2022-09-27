budget = float(input())
input_line = input()

total_price = 0
article_count = 0
while input_line != "Stop":
    price_article = float(input())
    article_count += 1
    if article_count % 3 == 0:
        total_price += (price_article / 2)
    else:
        total_price += price_article
    if total_price > budget:
        diff = abs(total_price - budget)
        print("You don't have enough money!")
        print(f"You need {diff:.2f} leva!")
        break
    input_line = input()

if input_line == "Stop":
    print(f"You bought {article_count} products for {total_price:.2f} leva.")
