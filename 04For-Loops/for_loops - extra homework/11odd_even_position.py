import sys

positions = int(input())

odd_sum = 0  # Нечетно
odd_min = sys.maxsize
odd_max = -sys.maxsize
even_sum = 0  # Четно
even_min = sys.maxsize
even_max = -sys.maxsize
odd_counter = 0
even_counter = 0
for i in range(1, positions + 1):
    inputNum = float(input())
    if i % 2 != 0:
        odd_sum += inputNum
        odd_counter += 1
        if inputNum <= odd_min:
            odd_min = inputNum
        if inputNum >= odd_max:
            odd_max = inputNum
    else:
        even_sum += inputNum
        even_counter += 1
        if inputNum <= even_min:
            even_min = inputNum
        if inputNum >= even_max:
            even_max = inputNum

print(f"OddSum={odd_sum:.2f},")
if odd_counter > 0:
    print(f"OddMin={odd_min:.2f},")
else:
    print(f"OddMin=No,")
if odd_counter>0:
   print(f"OddMax={odd_max:.2f},")
else:
    print(f"OddMax=No,")
print(f"EvenSum={even_sum:.2f},")
if even_counter > 0:
    print(f"EvenMin={even_min:.2f},")
else:
    print(f"EvenMin=No,")
if even_counter>0:
   print(f"EvenMax={even_max:.2f}")
else:
    print(f"EvenMax=No")

