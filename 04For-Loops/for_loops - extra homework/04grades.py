students = int(input())

top = 0
mid = 0
low = 0
fail = 0
count = 0

for i in range(1, students + 1):
    grade = float(input())
    count += grade
    if grade < 3:
        fail += 1
    elif grade < 4:
        low += 1
    elif grade < 5:
        mid += 1
    else:
        top += 1

top_percent = top / students * 100
print(f"Top students: {top_percent:.2f}%")
mid_percent = mid / students * 100
print(f"Between 4.00 and 4.99: {mid_percent:.2f}%")
low_percent = low / students * 100
print(f"Between 3.00 and 3.99: {low_percent:.2f}%")
fail_percent = fail / students * 100
print(f"Fail: {fail_percent:.2f}%")
average_grade = count / students
print(f"Average: {average_grade:.2f}")
