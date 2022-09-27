record_in_seconds=float(input())
distance_m=float(input())
time_for_1meter=float(input())
time=distance_m*time_for_1meter
delay=distance_m//15*12.5
total_time=delay+time
diference=total_time-record_in_seconds
if total_time<record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {diference:.2f} seconds slower.")