dayoffs = int(input())
workdrays = 365 - dayoffs
work_minutes = 63
off_minutes = 127
total_play = (dayoffs*off_minutes)+(work_minutes*workdrays)
if total_play > 30000 :
    more_play = total_play - 30000
    print("Tom will run away")
    print(f"{more_play// 60} hours and {more_play % 60} minutes more for play" )
else:
    unsuficient= 30000 - total_play
    print("Tom sleeps well")
    print(f"{unsuficient // 60} hours and {unsuficient % 60} minutes less for play")