cinemaCapacity = int(input())
command = input()

peopleQty = 0
totalPrice = 0

while command != "Movie time!":
    currentPeople = int(command)
    cinemaCapacity -= currentPeople
    if cinemaCapacity < 0:
        print("The cinema is full.")
        break
    else:
        if currentPeople % 3 == 0:
           currentPrice = currentPeople * 5 - 5
           totalPrice += currentPrice
        else:
           currentPrice = currentPeople * 5
           totalPrice += currentPrice
    command = input()
    if command == "Movie time!":
        print(f"There are {cinemaCapacity} seats left in the cinema.")
        break

print(f"Cinema income - {totalPrice} lv.")
