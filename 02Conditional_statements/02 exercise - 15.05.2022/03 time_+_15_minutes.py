hours = int(input())
minutes = int(input())
total_time = hours * 60 + minutes + 15
hours_output= total_time // 60
minutes_output= total_time % 60
if hours_output >23:
    hours_output=0
if minutes_output < 10:
    print(f"{hours_output}:0{minutes_output}")
else:
    print(f"{hours_output}:{minutes_output}")