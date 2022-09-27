number_one=int(input())
number_two=int(input())
number_tгree=int(input())

allowed_numbers=[2,3,5,7]

for one in range(2, number_one+1,2):
    for two in range(1,number_two+1):
        for trree in range(2,number_tгree+1,2):
            if two in allowed_numbers:
                print(one,two,trree)