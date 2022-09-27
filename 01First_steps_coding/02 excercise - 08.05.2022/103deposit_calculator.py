accaunt_balance=float(input())
months=int(input())
annual_rate=float(input())
per_year= accaunt_balance * (annual_rate/100)
per_mont=per_year/12
total_sum= accaunt_balance + per_mont *months
print(total_sum)
