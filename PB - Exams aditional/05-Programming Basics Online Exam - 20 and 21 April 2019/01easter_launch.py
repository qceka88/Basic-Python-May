cakeQty = int(input())
eggsPack = int(input())
cookiesKG = int(input())

priceCake = cakeQty * 3.2
eggsPrice = eggsPack * 4.35
cookiesPrice = cookiesKG * 5.40
paintPrice = eggsPack * 12 * 0.15

totalPrice = priceCake + eggsPrice + cookiesPrice + paintPrice

print(f"{totalPrice:.2f}")
