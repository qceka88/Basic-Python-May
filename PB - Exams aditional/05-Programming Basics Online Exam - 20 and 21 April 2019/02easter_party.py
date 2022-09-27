guestsQty = int(input())
singlePrice = float(input())
budgetDesi = float(input())

guestsPrice = guestsQty * singlePrice
cakePrice = budgetDesi * 0.10

if 10 <= guestsQty < 16:
    guestsPrice *= 0.85
elif 16< guestsQty <= 20:
    guestsPrice *= 0.80
elif 20 < guestsQty:
    guestsPrice *= 0.75

totalPrice = cakePrice + guestsPrice
diff = abs(budgetDesi - totalPrice)

if budgetDesi >= totalPrice:
    print(f"It is party time! {diff:.2f} leva left.")
else:
    print(f"No party! {diff:.2f} leva needed.")
