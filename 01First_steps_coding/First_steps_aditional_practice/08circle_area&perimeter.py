from math import pi

radius_r = float(input())
area = (radius_r ** 2) * pi
perimeter = radius_r * 2 * pi
print("{:.2f}".format(area))
print("{:.2f}".format(perimeter))
