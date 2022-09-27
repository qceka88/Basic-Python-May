fuel_type = input()
fuel_volume = float(input())
discount_card = input()

benzin = 2.22
diesel = 2.33
gas = 0.93

gas_price = gas * fuel_volume
diesel_price = diesel * fuel_volume
gasoline_price = benzin * fuel_volume

discount_gasoline = 0.18 * fuel_volume
discount_diesel = 0.12 * fuel_volume
discount_gas = 0.08 * fuel_volume

discount_20_25 = 0.92
dicount_25 = 0.90

if fuel_volume < 20:
    if discount_card == "Yes":
        if fuel_type == "Gas":
            price = gas_price - discount_gas
        elif fuel_type == "Gasoline":
            price = gasoline_price - discount_gasoline
        else:
            price = diesel_price - discount_diesel
    else:
        if fuel_type == "Gas":
            price = gas_price
        elif fuel_type == "Gasoline":
            price = gasoline_price
        else:
            price = diesel_price
elif fuel_volume <= 25:
    if discount_card == "Yes":
        if fuel_type == "Gas":
            price = (gas_price - discount_gas) * discount_20_25
        elif fuel_type == "Gasoline":
            price = (gasoline_price - discount_gasoline) * discount_20_25
        else:
            price = (diesel_price - discount_diesel) * discount_20_25
    else:
        if fuel_type == "Gas":
            price = gas_price * discount_20_25
        elif fuel_type == "Gasoline":
            price = gasoline_price * discount_20_25
        else:
            price = diesel_price * discount_20_25
else:
    if discount_card == "Yes":
        if fuel_type == "Gas":
            price = (gas_price - discount_gas) * dicount_25
        elif fuel_type == "Gasoline":
            price = (gasoline_price - discount_gasoline) * dicount_25
        else:
            price = (diesel_price - discount_diesel) * dicount_25
    else:
        if fuel_type == "Gas":
            price = gas_price * dicount_25
        elif fuel_type == "Gasoline":
            price = gasoline_price * dicount_25
        else:
            price = diesel_price * dicount_25

print(f"{price:.2f} lv.")
