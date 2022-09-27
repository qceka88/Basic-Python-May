input_line = input()

student_count = 0
adult_count = 0
kid_count = 0
total_ticket = 0
while input_line != "Finish":
    seats = int(input())
    movie = input_line
    current_tickets = 0
    for i in range(1, seats + 1):
        ticket = input()

        if ticket == "student":
            student_count += 1
        elif ticket == "standard":
            adult_count += 1
        elif ticket == "kid":
            kid_count += 1
        if ticket == "End":
            break
        total_ticket += 1
        current_tickets += 1
    input_line = input()

    movie_percent = current_tickets / seats * 100
    print(f"{movie} - {movie_percent:.2f}% full.")

kid_percent = kid_count / total_ticket * 100
adult_count = adult_count / total_ticket * 100
student_percent = student_count / total_ticket * 100

print(f"Total tickets: {total_ticket}")
print(f"{student_percent:.2f}% student tickets.")
print(f"{adult_count:.2f}% standard tickets.")
print(f"{kid_percent:.2f}% kids tickets.")
