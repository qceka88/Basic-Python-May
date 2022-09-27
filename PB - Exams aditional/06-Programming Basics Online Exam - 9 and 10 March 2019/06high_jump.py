requiredHigh = int(input())

startHigh = requiredHigh - 30
finalJump = 0
jumpCounter = 0
sucsess = True
for jump in range(startHigh, requiredHigh + 1, 5):
    for i in range(1, 3 + 1):
        currentTry = int(input())
        jumpCounter += 1
        finalJump = jump
        if currentTry > jump:
            sucsess = True
            break
        if i == 3:
            sucsess = False
            break
    if sucsess is not True:
        break

if sucsess:
    print(f"Tihomir succeeded, he jumped over {finalJump}cm after {jumpCounter} jumps.")
else:
    print(f"Tihomir failed at {finalJump}cm after {jumpCounter} jumps.")
