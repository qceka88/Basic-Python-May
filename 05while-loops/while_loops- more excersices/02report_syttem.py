needed_sum = int(input())
command = input()

sum_card = 0
sum_cash = 0
saved_sum = 0
card_pay = 0
cash_pay = 0
count_pay = 0
while command != "End":
    current_pay = int(command)
    count_pay += 1
    if count_pay % 2 == 0 and current_pay >= 10:
        card_pay += 1
        sum_card += current_pay
        saved_sum += current_pay
        print("Product sold!")
    elif count_pay % 2 != 0 and current_pay <= 100:
        cash_pay += 1
        sum_cash += current_pay
        saved_sum += current_pay
        print("Product sold!")
    else:
        print("Error in transaction!")
    if saved_sum >= needed_sum:
        average_card = sum_card / card_pay
        average_cash = sum_cash / cash_pay
        print(f"Average CS: {average_cash:.2f}")
        print(f"Average CC: {average_card:.2f}")
        break
    command = input()
    if command == "End":
        print("Failed to collect required money for charity.")
        break
