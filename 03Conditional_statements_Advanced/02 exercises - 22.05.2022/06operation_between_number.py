first_num = int(input())
second_num = int(input())
operator = input()

zero_flag = False
result = 0
even_or_odd = ""

if operator == "+":
    result = first_num + second_num
elif operator == "-":
    result = first_num - second_num
elif operator == "*":
    result = first_num * second_num
elif operator == "/":
    if second_num == 0:
        zero_flag=True
    else:
        result = first_num / second_num
elif operator == "%":
    if second_num == 0:
        zero_flag=True
    else:
        result = first_num % second_num


if zero_flag:
    print(f"Cannot divide {first_num} by zero")
elif operator == "+" or operator == "-" or operator == "*":
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{first_num} {operator} {second_num} = {result} - {even_or_odd}")
elif operator == "%":
    print(f"{first_num} {operator} {second_num} = {result}")
elif operator == "/":
    print(f"{first_num} {operator} {second_num} = {result:.2f}")