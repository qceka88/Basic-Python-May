actorName = input()
initialScores = float(input())
bursarQty = int(input())

totalScores = initialScores
reachedScores = False
for i in range(1, bursarQty + 1):
    nameCurrent = input()
    currentScores = float(input())

    totalScores += ((len(nameCurrent) * currentScores) / 2)
    if totalScores >= 1250.5:
        reachedScores = True
        break

if reachedScores:
    print(f"Congratulations, {actorName} got a nominee for leading role with {totalScores:.1f}!")
else:
    neededScores = 1250.5 - totalScores
    print(f"Sorry, {actorName} you need {neededScores:.1f} more!")
