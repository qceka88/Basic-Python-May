totalEggs = int(input())

redCounter = 0
orangeCounter = 0
blueCounter = 0
greenCounter = 0

for i in range(1, totalEggs + 1):
    color = input()
    if color == "red":
        redCounter += 1
    elif color == "orange":
        orangeCounter += 1
    elif color == "blue":
        blueCounter += 1
    elif color == "green":
        greenCounter += 1

maxEggs= max(redCounter,orangeCounter,greenCounter,blueCounter)
maxColor = ""

if redCounter == maxEggs:
    maxColor = "red"
if orangeCounter  == maxEggs:
    maxColor = "orange"
if blueCounter == maxEggs:
    maxColor = "blue"
if greenCounter == maxEggs:
    maxColor = "green"


print(f"Red eggs: {redCounter}")
print(f"Orange eggs: {orangeCounter}")
print(f"Blue eggs: {blueCounter}")
print(f"Green eggs: {greenCounter}")
print(f"Max eggs: {maxEggs} -> {maxColor}")
