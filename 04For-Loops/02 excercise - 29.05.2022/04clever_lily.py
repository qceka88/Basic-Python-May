age = int(input())
price_laundry = float(input())
price_toy = int(input())

money = 10
count_toys = 0
sum = 0
brother_count = 0

for years in range(1, age + 1):
    if years % 2 != 0:
        count_toys += 1
    else:
        brother_count += 1
        sum = sum + money
        money = money + 10

result = sum + (count_toys * price_toy) - brother_count
diff = abs(result - price_laundry)

if result >= price_laundry:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
