month=input()
days=int(input())

price_apart=0
price_studio=0

if month =="May" or month == "October":
    price_studio=days*50
    price_apart=days*65
    if 7 < days < 14:
        price_studio=price_studio*0.95
    elif days >14:
        price_studio=price_studio*0.7
        price_apart=price_apart*0.90
elif month == "June" or month == "September":
    price_studio = days * 75.2
    price_apart = days * 68.7
    if 7 < days < 14:
        price_studio=price_studio*0.95
    elif days >14:
        price_studio=price_studio*0.8
        price_apart=price_apart*0.90
elif month == "July" or month == "August":
    price_studio = days * 76
    price_apart = days * 77
    if days > 14:
        price_apart=price_apart*0.9

print(f"Apartment: {price_apart:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")