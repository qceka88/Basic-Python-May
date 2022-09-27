name = input()
clas = 1
bad_fails = 0
total_grade = 0
is_exludet = False

while clas <= 12:
    current_grade = float(input())
    if current_grade < 4:
        bad_fails += 1
        if bad_fails == 2:
            is_exludet = True
            break
    else:
        total_grade += current_grade
        clas += 1

if is_exludet:
    print(f"{name} has been excluded at {clas} grade")
else:
    average_grade = total_grade / 12
    print(f"{name} graduated. Average grade: {average_grade:.2f}")
