city = input()
sales = float(input())
commision = 0
if 0 <= sales <= 500:
    if city == "Sofia":
        commision = 0.05
    elif city == "Varna":
        commision = 0.045
    elif city == "Plovdiv":
        commision = 0.055
elif 500 < sales <= 1000:
    if city == "Sofia":
        commision = 0.07
    elif city == "Varna":
        commision = 0.075
    elif city == "Plovdiv":
        commision = 0.08
elif 1000 < sales <= 10000:
    if city == "Sofia":
        commision = 0.08
    elif city == "Varna":
        commision = 0.10
    elif city == "Plovdiv":
        commision = 0.12
elif sales > 10000:
    if city == "Sofia":
        commision = 0.12
    elif city == "Varna":
        commision = 0.13
    elif city == "Plovdiv":
        commision = 0.145
if commision == 0:
    print("error")
else:
  income=(sales * commision)
  print(f"{income:.2f}")
