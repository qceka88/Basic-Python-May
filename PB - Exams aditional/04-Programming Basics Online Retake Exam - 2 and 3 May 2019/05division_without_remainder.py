inputNumber = int(input())

twoCounter = 0
threeCounter = 0
fourCounter = 0
totalCounter = 0
for i in range(1, inputNumber + 1):
    currentNumber = int(input())
    totalCounter += 1
    if currentNumber % 2 == 0:
        twoCounter += 1
    if currentNumber % 3 == 0:
        threeCounter += 1
    if currentNumber % 4 == 0:
        fourCounter += 1

twoPercent = twoCounter / totalCounter * 100
threePercent = threeCounter / totalCounter * 100
fourPercent = fourCounter / totalCounter * 100

print(f"{twoPercent:.2f}%")
print(f"{threePercent:.2f}%")
print(f"{fourPercent:.2f}%")
