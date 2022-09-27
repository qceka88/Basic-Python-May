last_sector = ord(input())
rows_qty = int(input())
seats_qty = int(input())
seats = 0
counter = 0
for sectors in range(65, last_sector + 1):
    for row in range(1, rows_qty + 1):
        if row % 2 == 0:
            seats = seats_qty + 2
        else:
            seats = seats_qty
        seat_num = 96
        for seat in range(1, seats + 1):
            seat_num += 1
            print(f"{chr(sectors)}{row}{chr(seat_num)}")
            counter += 1
    rows_qty += 1
print(counter)