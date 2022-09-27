size_eggs = input()
color_eggs = input()
batch_qty = int(input())

if size_eggs == "Large":
    if color_eggs == "Red":
        price_eggs = 16
    elif color_eggs == "Green":
        price_eggs = 12
    elif color_eggs == "Yellow":
        price_eggs = 9
elif size_eggs == "Medium":
    if color_eggs == "Red":
        price_eggs = 13
    elif color_eggs == "Green":
        price_eggs = 9
    elif color_eggs == "Yellow":
        price_eggs = 7
elif size_eggs == "Small":
    if color_eggs == "Red":
        price_eggs = 9
    elif color_eggs == "Green":
        price_eggs = 8
    elif color_eggs == "Yellow":
        price_eggs = 5

price_batches = batch_qty * price_eggs
after_taxes = price_batches * 0.65

print(f"{after_taxes:.2f} leva.")
