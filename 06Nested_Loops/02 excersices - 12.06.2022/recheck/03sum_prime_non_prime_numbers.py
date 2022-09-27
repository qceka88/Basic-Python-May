input_line = input()

prime_number = 0
non_prime_number = 0
while input_line != "stop":
    current_num = int(input_line)

    if current_num < 0:
        print("Number is negative.")
        input_line = input()
        continue
    prime_counter = 0
    for i in range(1, current_num + 1):
        if current_num % i == 0:
            prime_counter += 1
    if prime_counter == 2:
        prime_number += current_num
        prime_counter = 0
    else:
        non_prime_number += current_num
    input_line = input()

print(f"Sum of all prime numbers is: {prime_number}")
print(f"Sum of all non prime numbers is: {non_prime_number}")
