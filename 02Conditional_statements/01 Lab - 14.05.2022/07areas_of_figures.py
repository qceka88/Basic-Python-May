from math import pi

type_of_the_figure= input()
result= 0
if type_of_the_figure == "square":
    side = float(input())
    result= side * side
elif type_of_the_figure == "rectangle":
    first_side = float(input())
    second_side = float(input())
    result = first_side * second_side
elif type_of_the_figure == "circle":
    radius = float(input())
    result =  pi * radius ** 2
else:
    side = float(input())
    height = float(input())
    result = side * height / 2
print(f"{result:.3f}")