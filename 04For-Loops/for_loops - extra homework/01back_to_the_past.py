money = float(input())
year = int(input())

years_to_live = year - 1800
sum_odd = 0
sum_even = 0
old_ivan = 17
for wealth in range(years_to_live + 1):
    old_ivan += 1
    if wealth % 2 == 0:
        per_year1 = 12000
        sum_even += per_year1
    else:
        per_year2 = 12000 + 50 * old_ivan
        sum_odd += per_year2

total_expences = sum_odd + sum_even

total_sum = abs(money - total_expences)
if money >= total_expences:
    print(f"Yes! He will live a carefree life and will have {total_sum:.2f} dollars left.")
else:
    print(f"He will need {total_sum:.2f} dollars to survive.")
