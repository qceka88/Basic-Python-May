line_input = input()

total_tickets = 0
student_count = 0
standard_count = 0
kid_count = 0
while line_input != "Finish":
    movie = line_input
    capacity = int(input())

    command_line = input()
    current_movie_counter = 0
    while command_line != "End":
        type_ticket = command_line
        total_tickets += 1
        current_movie_counter += 1
        if type_ticket == "student":
            student_count += 1
        elif type_ticket == "standard":
            standard_count += 1
        else:
            kid_count += 1

        if current_movie_counter == capacity:
            break
        command_line = input()
    percent_cur_movie = current_movie_counter / capacity * 100
    print(f"{movie} - {percent_cur_movie:.2f}% full.")

    line_input = input()
student_percent = student_count / total_tickets * 100
standard_percent = standard_count / total_tickets * 100
kid_percent = kid_count / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{student_percent:.2f}% student tickets.")
print(f"{standard_percent:.2f}% standard tickets.")
print(f"{kid_percent:.2f}% kids tickets.")