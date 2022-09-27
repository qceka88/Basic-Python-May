start_num = int(input())
finish_num = int(input())
for number1 in range(start_num, finish_num + 1):
    for number2 in range(start_num, finish_num + 1):
        for number3 in range(start_num, finish_num + 1):
            for number4 in range(start_num, finish_num + 1):
                if number1 % 2 == 0 and number4 % 2 != 0 or number1 % 2 != 0 and number4 % 2 == 0:
                    if number1 > number4 and (number2 + number3) % 2 == 0:
                        print(f"{number1}{number2}{number3}{number4}", end=" ")
