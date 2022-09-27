budget = float(input())
night_qty = int(input())
price_night = float(input())
extra_spend = int(input())

extra_expences = extra_spend * budget / 100

if night_qty > 7:
    discount = price_night * 0.95
    total_price = extra_expences + discount * night_qty
else:
    total_price = extra_expences + night_qty * price_night

diff = abs(total_price - budget)
if total_price <= budget:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")
