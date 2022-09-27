first_start = int(input())
second_start = int(input())
diff01 = int(input())
diff02 = int(input())

fisrt_stop = first_start + diff01
second_stop = second_start + diff02

first_prime = False
second_prime = False
for i in range(first_start, fisrt_stop + 1):
    first_counter = 0
    for prime01 in range(1, i + 1):
        if i % prime01 == 0:
            first_counter += 1
    if first_counter == 2:
        first_prime = True
    if first_prime:
        for j in range(second_start, second_stop + 1):
            second_counter = 0
            for prime02 in range(1, j + 1):
                if j % prime02 == 0:
                    second_counter += 1
            if second_counter == 2:
                second_prime = True
            if first_prime and second_prime:
                print(f"{i}{j}")
                second_prime=False
        first_prime = False