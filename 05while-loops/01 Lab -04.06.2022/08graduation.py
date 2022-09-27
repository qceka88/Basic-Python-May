name_of_student = input()
current_class = 1
bad_tries = 0
total_grade = 0
is_excludet = False

while current_class <= 12:
    current_grade = float(input())
    if current_grade < 4:
        bad_tries += 1
        if bad_tries > 1:
            is_excludet = True
            break
    else:
        current_class += 1
        total_grade += current_grade
if is_excludet:
    print(f"{name_of_student} has been excluded at {current_class} grade")
else:
    averrage_grade = total_grade / 12
    print(f"{name_of_student} graduated. Average grade: {averrage_grade:.2f}")
