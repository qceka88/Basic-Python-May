from math import ceil, floor

paint_cans_qty = int(input())
wallpaper_qty = int(input())
price_gloves = float(input())
brush_price = float(input())

paint_total_price = paint_cans_qty * 21.5
wallpaper_total_price = wallpaper_qty * 5.20

gloves_qty = ceil(wallpaper_qty * 0.35)
brush_qty = floor(paint_cans_qty * 0.48)

gloves_total_price = gloves_qty * price_gloves
brushes_total_price = brush_price * brush_qty

total_price = paint_total_price + wallpaper_total_price + gloves_total_price + brushes_total_price
delivery_price=total_price/15

print(f"This delivery will cost {delivery_price:.2f} lv.")
