days = int(input())
rakia_total = 0
degree_count = 0

for baking in range(days):
    rakia_daily = float(input())
    rakia_degree = float(input())
    rakia_total += rakia_daily
    degree_count += rakia_degree * rakia_daily

average_degree = degree_count / rakia_total

print(f"Liter: {rakia_total:.2f}")
print(f"Degrees: {average_degree:.2f}")

if average_degree < 38:
    print("Not good, you should baking!")
elif average_degree < 42:
    print("Super!")
else:
    print("Dilution with distilled water!")
