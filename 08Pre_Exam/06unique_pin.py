num01 = int(input())
num02 = int(input())
num03 = int(input())

value02 = [2, 3, 5, 7]

for i in range(2, num01 + 1, 2):
    for k in range(1, num02 + 1):
        for l in range(2, num03 + 1, 2):
            if k in value02:
                print(i, k, l)


