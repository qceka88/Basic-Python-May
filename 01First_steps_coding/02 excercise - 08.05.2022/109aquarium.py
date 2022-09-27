long_cm=int(input())
width_cm=int(input())
height_cm=int(input())
percetage_add=float(input())
aquarium_volume= long_cm *width_cm *height_cm
volume_litter=aquarium_volume/1000
dry_volume=percetage_add/100
water_folume=volume_litter*(1-dry_volume)
print(water_folume)