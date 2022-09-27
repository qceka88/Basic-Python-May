start = int(input())
end = int(input())

for i in range(start, end + 1):
    current_str = str(i)
    odd_sum = 0
    even_sum = 0
    for symbol_count in range(len(current_str)):
        digit=int(current_str[symbol_count])
        if symbol_count % 2 == 0:
            even_sum += digit
        else:
            odd_sum+=digit
    if even_sum==odd_sum:
        print(f"{current_str}", end=" ")

