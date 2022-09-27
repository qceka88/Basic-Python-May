from math import ceil
name=str(input())
episode_time=int(input())
break_time=int(input())
eating_time=break_time/8
resting=break_time/4
needed_time=eating_time+resting
left_time=break_time-needed_time
difference=abs(break_time-needed_time-episode_time)
if episode_time <= left_time:
    print(f"You have enough time to watch {name} and left with {ceil(difference)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name}, you need {ceil(difference)} more minutes.")