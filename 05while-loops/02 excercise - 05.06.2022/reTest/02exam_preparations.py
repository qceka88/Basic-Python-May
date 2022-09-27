poor_grades = int(input())
input_line = input()
all_grade_sum = 0
count_grades = 0
bad_grades = 0
last_problem = ""
while input_line != "Enough":
    last_problem = input_line
    current_grade = int(input())
    if current_grade <= 4:
        bad_grades += 1
        if bad_grades >= poor_grades:
            break
    input_line = input()
    count_grades += 1
    all_grade_sum += current_grade

if bad_grades >= poor_grades:
    print(f"You need a break, {bad_grades} poor grades.")
else:
    average_grade = all_grade_sum / count_grades
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {count_grades}")
    print(f"Last problem: {last_problem}")
