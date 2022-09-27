minutes_input = int(input())
seconds_input = int(input())
distance = float(input())
seconds_for_meters = int(input())
control_seconds = minutes_input * 60 + seconds_input

acceleration_seconds = distance / 120 * 2.5
racer_time = distance / 100 * seconds_for_meters - acceleration_seconds

if racer_time <= control_seconds:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {racer_time:.3f}.")
else:
    diff = abs(control_seconds - racer_time)
    print(f"No, Marin failed! He was {diff:.3f} second slower.")
