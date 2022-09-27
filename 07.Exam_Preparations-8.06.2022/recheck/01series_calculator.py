name_of_series = input()
num_of_seasons = int(input())
episodes_number = int(input())
time_of_episode = float(input())

full_time_episode = time_of_episode * 1.2

last_episode = num_of_seasons * 10

total_time = full_time_episode *episodes_number * num_of_seasons + last_episode


print(f"Total time needed to watch the {name_of_series} series is {int(total_time)} minutes.")