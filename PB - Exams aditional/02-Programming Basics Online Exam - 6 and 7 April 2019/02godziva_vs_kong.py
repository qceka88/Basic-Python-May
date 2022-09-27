movie_budged = float(input())
qty_statists = int(input())
single_suit_price = float(input())

decor_price = movie_budged * 0.10

if qty_statists > 150:
    price_suits = single_suit_price * qty_statists * 0.9
else:
    price_suits = single_suit_price * qty_statists

total_price = price_suits + decor_price
diff = abs(movie_budged - total_price)
if total_price <= movie_budged:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")

