screening_type= input()
rows=int(input())
columns=int(input())

all_seats=rows*columns
premiere=12
normal=7.5
discount=5
price=0
if screening_type == "Premiere":
    price=all_seats*premiere
elif screening_type == "Normal":
    price=all_seats*normal
elif screening_type == "Discount":
    price=all_seats*discount
print(f"{price:.2f} leva")