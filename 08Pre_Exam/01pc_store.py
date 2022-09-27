cpu_price = float(input())
gpu_price = float(input())
single_ram_price = float(input())
ram_qty = int(input())
discount = float(input())

ram_price_lv = single_ram_price * ram_qty * 1.57
cpu_discount_lv= (cpu_price - (cpu_price*discount))*1.57
gpu_discount_lv= (gpu_price - (gpu_price*discount))*1.57

total_lv = ram_price_lv+cpu_discount_lv+gpu_discount_lv

print(f"Money needed - {total_lv:.2f} leva.")
