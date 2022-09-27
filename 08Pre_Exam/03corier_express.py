weight = float(input())
type = input()
distance = int(input())
transport = 0
price = 0
if type == "standard":
    if weight < 1:
        price = distance * 0.03
    elif weight < 10:
        price = distance * 0.05
    elif weight < 40:
        price = distance * 0.1
    elif weight < 90:
        price = distance * 0.15
    elif weight < 150:
        price = distance * 0.20
elif type == "express":
    if weight < 1:
        transport = distance * 0.03
        weight_add = ((0.03 * 0.8) * weight) * distance
        price = weight_add + transport
    elif weight < 10:
        transport = distance * 0.05
        weight_add = ((0.05 * 0.4) * weight) * distance
        price = weight_add + transport
    elif weight < 40:
        transport = distance * 0.1
        weight_add = ((0.1 * 0.05) * weight) * distance
        price = weight_add + transport
    elif weight < 90:
        transport = distance * 0.15
        weight_add = ((0.15 * 0.02) * weight) * distance
        price = weight_add + transport
    elif weight < 150:
        transport = distance * 0.20
        weight_add = ((0.20 * 0.01) * weight) * distance
        price = weight_add + transport

print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {price:.2f} lv.")
