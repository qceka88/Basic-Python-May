side_x=float(input())
side_y=float(input())
roof_h=float(input())
door_x=1.2*2
window_y= 1.5 * 1.5
heith=side_x
area_y=((side_y*side_x)*2)-(window_y*2)
area_x=((side_x*side_x)*2)-door_x
green=(area_y+area_x)/3.4
print("{:.2f}".format(green))
area_yroof=(side_y*side_x)*2
area_xroof=2*(side_x*roof_h/2)
red=(area_xroof+area_yroof)/4.3
print("{:.2f}".format(red))