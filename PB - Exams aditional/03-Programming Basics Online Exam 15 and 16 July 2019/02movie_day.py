timeForShoots = int(input())
scenesQty = int(input())
scenesTime = int(input())

timePrepearing =timeForShoots * 0.15

filmingTime= scenesQty * scenesTime + timePrepearing

diff=abs(timeForShoots-filmingTime)


if timeForShoots >= filmingTime:
    print(f"You managed to finish the movie on time! You have {round(diff)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(diff)} minutes.")