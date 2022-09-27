number_people = int(input())
input_line = input()
total_grade = 0
counter = 0
while input_line != "Finish":
    discipline = input_line
    sum_grade_cur = 0
    for i in range(1, number_people + 1):
        current_grade = float(input())
        sum_grade_cur += current_grade
        total_grade += current_grade
        counter += 1
    average_cur_grade = sum_grade_cur / number_people
    input_line = input()
    print(f"{discipline} - {average_cur_grade:.2f}.")
total_average = total_grade / counter
print(f"Student's final assessment is {total_average:.2f}.")
judges = int(input())
input_line = input()

total_grade = 0
total_counter = 0
while input_line != "Finish":
    discipline = input_line

    cur_dis_grade = 0
    for i in range(1, judges + 1):
        current_grade = float(input())
        cur_dis_grade += current_grade
        total_grade += current_grade
        total_counter += 1

    averrage_dis_grade = cur_dis_grade / judges
    print(f"{discipline} - {averrage_dis_grade:.2f}.")
    input_line = input()
tot_average_grade = total_grade / total_counter
print(f"Student's final assessment is {tot_average_grade:.2f}.")
