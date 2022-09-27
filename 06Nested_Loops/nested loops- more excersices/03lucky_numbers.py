input_number = int(input())

if input_number > 10:
    number = 10
else:
    number = input_number

for num01 in range(1, number):
    for num02 in range(1, number):
        for num03 in range(1, number):
            for num04 in range(1, number):
                if (num01 + num02) == (num03 + num04) and input_number % (num01 + num02) == 0:
                    print(f"{num01}{num02}{num03}{num04}", end=" ")
