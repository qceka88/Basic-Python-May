season = input()
group_type = input()
students = int(input())
days = int(input())

sport = ""
price = 0

if season == "Winter":
    if group_type == "boys":
        price = students * days * 9.6
        sport = "Judo"
    elif group_type == "girls":
        sport = "Gymnastics"
        price = students * days * 9.6
    elif group_type == "mixed":
        sport = "Ski"
        price = students *days* 10
elif season == "Spring":
    if group_type == "boys":
        price = students * days * 7.2
        sport = "Tennis"
    elif group_type == "girls":
        sport = "Athletics"
        price = students * days * 7.2
    elif group_type == "mixed":
        sport = "Cycling"
        price = students *days* 9.50
elif season == "Summer":
    if group_type == "boys":
        price = students * days * 15
        sport = "Football"
    elif group_type == "girls":
        sport = "Volleyball"
        price = students * days * 15
    elif group_type == "mixed":
        sport = "Swimming"
        price = students *days* 20

if students >= 50:
    price = price * 0.5
elif students >= 20:
    price = price * 0.85
elif students >= 10:
    price = price * .95

print(f"{sport} {price:.2f} lv.")