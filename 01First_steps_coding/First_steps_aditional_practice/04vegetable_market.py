vegetables_price=float(input())
fruits_price=float(input())
vegetables_weight=float(input())
fruits_weight=float(input())
vege_profit= vegetables_price * vegetables_weight
fruit_profit= fruits_price * fruits_weight
total_profit= float((vege_profit+fruit_profit)/1.94)
print("{:.2f}".format(total_profit))