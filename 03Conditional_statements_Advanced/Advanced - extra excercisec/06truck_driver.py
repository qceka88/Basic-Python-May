season=input()
distance=float(input())

salary=0
if distance<=5000:
    if season=="Spring" or season=="Autumn":
        salary=distance*0.75
    elif season == "Summer":
        salary=distance*0.9
    elif season=="Winter":
        salary=distance*1.05
elif distance <=10000:
    if season=="Spring" or season=="Autumn":
        salary=distance*0.95
    elif season == "Summer":
        salary=distance*1.10
    elif season=="Winter":
        salary=distance*1.25
elif distance <=20000:
    salary = distance * 1.45

total_salary = salary * 4
after_taxes=total_salary*0.9

print(f"{after_taxes:.2f}")
