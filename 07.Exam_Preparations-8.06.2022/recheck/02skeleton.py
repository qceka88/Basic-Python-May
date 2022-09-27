control_minutes = int(input())
control_seconds = int(input())
distance_meteres = float(input())
seconds_per_hundred_meters = int(input())

control_time = control_minutes * 60 + control_seconds
acceleration = distance_meteres / 120 * 2.5

race_time = (distance_meteres/100)*seconds_per_hundred_meters - acceleration

if race_time <= control_time:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {race_time:.3f}.")
else:
    needed_time =   abs(race_time - control_time)
    print(f"No, Marin failed! He was {needed_time:.3f} second slower.")
