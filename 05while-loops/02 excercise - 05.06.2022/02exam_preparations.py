poor_grades = int(input())
input_line = input()
sum_all_gares = 0
count_grades = 0
last_problem = ""
poor_grades_count = 0
while input_line != "Enough":
    last_problem = input_line
    current_grade = int(input())
    if current_grade <= 4:
        poor_grades_count += 1
    count_grades += 1
    sum_all_gares += current_grade

    if poor_grades_count >= poor_grades:
        break
    input_line = input()
if poor_grades_count == poor_grades:
    print(f"You need a break, {poor_grades_count} poor grades.")
else:
    avg_grade = sum_all_gares / count_grades
    print(f"Average score: {avg_grade:.2f}")
    print(f"Number of problems: {count_grades}")
    print(f"Last problem: {last_problem}")
