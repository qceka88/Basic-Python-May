budget=float(input())
vga_count=int(input())
cpu_count=int(input())
ram_count=int(input())

vga_price=vga_count*250
cpu_price=vga_price*cpu_count*0.35
ram_price=ram_count*vga_price*0.10

total_price=vga_price+cpu_price+ram_price
if vga_count > cpu_count:
    total_price=total_price*0.85

diference=abs(budget-total_price)
if total_price<=budget:
    print(f"You have {diference:.2f} leva left!")
else:
    print(f"Not enough money! You need {diference:.2f} leva more!")