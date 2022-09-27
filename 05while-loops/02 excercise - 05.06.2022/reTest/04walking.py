input_line = input()
total_steps = 0

while input_line != "Going home":
    steps = int(input_line)
    total_steps += steps

    if total_steps >= 10000:
        break

    input_line = input()

if input_line == "Going home":
    steps_to_home = int(input())
    total_steps += steps_to_home

diff = abs(total_steps - 10000)
if total_steps >= 10000:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")