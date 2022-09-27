sea_offer = int(input())
mountain_offer = int(input())

input_line = input()
profit = 0
is_sold=False
while input_line != "Stop":

    if input_line == "sea":
        if sea_offer > 0:
            sea_offer-= 1
            profit += 680
    elif input_line == "mountain":
        if mountain_offer > 0:
            mountain_offer -= 1
            profit += 499
    if sea_offer == 0 and mountain_offer == 0:
        is_sold=True
        print("Good job! Everything is sold.")
        break
    input_line = input()

print(f"Profit: {profit} leva.")


