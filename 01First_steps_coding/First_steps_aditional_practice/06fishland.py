skumria=float(input())
caca=float(input())
midi=float(7.50)
palamud_mass=float(input())
safrid_mass=float(input())
mussels_mass=float(input())
palamud_price = skumria * palamud_mass *1.6
safrid_price=caca*safrid_mass*1.8
mussels_price=midi*mussels_mass
total_bill=palamud_price+safrid_price+mussels_price
print("{:.2f}".format(total_bill))