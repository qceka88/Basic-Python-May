month = int(input())

el_bill = 0
water = 0
internet = 0


for bill in range(1, month + 1):
    electricity = float(input())
    el_bill += electricity
    water += 20
    internet += 15

other = (el_bill + water + internet) * 1.2
average = (other + water + el_bill + internet) / month

print(f"Electricity: {el_bill:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {other:.2f} lv")
print(f"Average: {average:.2f} lv")