num = int(input())
cur_num = 1
for row in range(1, num + 1):
    for column in range(1, row + 1):
        if cur_num>num:
            break

        print(f"{cur_num}" , end=" ")
        cur_num+=1
    if cur_num > num:
        break
    print()