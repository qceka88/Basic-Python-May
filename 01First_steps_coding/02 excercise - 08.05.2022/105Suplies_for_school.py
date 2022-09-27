pen_count=int(input())
marker_count=int(input())
detergent_liters=int(input())
discount_percent=int(input())
price_pen= pen_count * 5.8
price_marker= marker_count * 7.2
price_detergent= detergent_liters *  1.2
total_price = price_pen+price_detergent+price_marker
price_with_discount= total_price-(total_price*(discount_percent/100))
print(price_with_discount)