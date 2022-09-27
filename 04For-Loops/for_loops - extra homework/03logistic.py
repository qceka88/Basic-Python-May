count = int(input())

bus_load = 0
truck_load = 0
train_load = 0

for i in range(1, count + 1):
    load_ton = int(input())
    if load_ton <= 3:
        bus_load = bus_load + load_ton
    elif load_ton <= 11:
        truck_load = truck_load + load_ton
    else:
        train_load = train_load + load_ton

total_load = bus_load + truck_load + train_load
bus_cost = bus_load * 200
truck_cost = truck_load * 175
train_cost = train_load * 120

average_cost = (bus_cost + train_cost + truck_cost) / total_load

print(f"{average_cost:.2f}")

bus_percent = bus_load / total_load * 100
print(f"{bus_percent:.2f}%")
truck_percent = truck_load / total_load * 100
print(f"{truck_percent:.2f}%")
train_percent = train_load / total_load * 100
print(f"{train_percent:.2f}%")
