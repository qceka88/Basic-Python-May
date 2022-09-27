days = int(input()) - 1
room_type = input()
approval = input()

room_for_one_person = 18
apartment = 25
president_apartment = 35

price = 0
if room_type == "room for one person":
    price = days * room_for_one_person
elif room_type == "apartment":
    if days < 10:
        price = days * apartment * 0.70
    elif 10 <= days <= 15:
        price = days * apartment * 0.65
    else:
        price = days * apartment * 0.5
elif room_type == "president apartment":
    if days < 10:
        price = days * president_apartment * 0.90
    elif 10 <= days <= 15:
        price = days * president_apartment * 0.85
    else:
        price = days * president_apartment * 0.8
if approval == "negative":
    price = price * 0.9
elif approval == "positive":
    price = price * 1.25

print(f"{price:.2f}")
