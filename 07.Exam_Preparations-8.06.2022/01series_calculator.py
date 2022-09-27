seires_name = input()
sasons = int(input())
episodes = int(input())
time_per_episode = float(input())

time_per_episode *= 1.2

last_episode = sasons * 10

total_time = sasons * episodes * time_per_episode + last_episode

print(f"Total time needed to watch the {seires_name} series is {int(total_time)} minutes.")


