let01 = ord(input())
let02 = ord(input())
let03 = ord(input())
counter = 0
for letter01 in range(let01, let02 + 1):
    for letter02 in range(let01, let02 + 1):
        for letter03 in range(let01, let02 + 1):
            if letter02 != let03:
                second_letter = letter02
            if letter01 != let03:
                first_letter = letter01
            if letter03 != let03:
                third_letter = letter03
            if letter01 != let03 and letter02 != let03 and letter03 != let03:
                counter += 1
                print(f"{chr(first_letter)}{chr(second_letter)}{chr(third_letter)}", end=" ")
print(counter)