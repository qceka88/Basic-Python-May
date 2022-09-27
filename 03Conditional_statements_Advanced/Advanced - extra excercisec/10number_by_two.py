number=float(input())

if number >= 0:
  while number >= 0:
        if number >=0:
           number = number * 2
           print(f"Result: {number:.2f}")
           number = float(input())
           if number<0:
              print("Negative number!")
else:
    print("Negative number!")