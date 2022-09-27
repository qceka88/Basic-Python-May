strawberriesPrice = float(input())
bananasKG = float(input())
orangesKG = float(input())
raspberriesKG = float(input())
strawberriesKG = float(input())

raspberriesPrice = strawberriesPrice / 2
orangesPrice = raspberriesPrice * 0.6
banansPrice = raspberriesPrice * 0.2

totalStrawberries = strawberriesPrice * strawberriesKG
totalBananas = bananasKG * banansPrice
totalOranges = orangesKG * orangesPrice
totalRaspberries = raspberriesKG * raspberriesPrice

neededMoney = totalRaspberries + totalOranges + totalBananas + totalStrawberries

print(f"{neededMoney:.2f}")