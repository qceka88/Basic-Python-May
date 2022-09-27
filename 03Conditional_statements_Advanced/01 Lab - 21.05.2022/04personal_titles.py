years=float(input())
gender=input()

if gender == "f":
    if years<16:
        print("Miss")
    else:
        print("Ms.")
else:
    if years<16:
        print("Master")
    else:
        print("Mr.")