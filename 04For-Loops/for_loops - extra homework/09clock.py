hour = 0
minutes = 0
for hour in range(0, 24):
    minutes = 0
    print(f"{hour} : {minutes}")
    for min in range(59):
        minutes += 1
        print(f"{hour} : {minutes}")
        if min == 59:
            hour += 1
