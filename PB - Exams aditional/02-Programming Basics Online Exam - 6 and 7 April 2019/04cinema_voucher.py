voucher = int(input())
inputLine = input()

counterTickets = 0
counterOthers = 0

while inputLine != "End":
    command = len(inputLine)
    if command > 8:
        symbol01 = ord(inputLine[0])
        symbol02 = ord(inputLine[1])
        ticketPrice = symbol01 + symbol02
        voucher -= ticketPrice
        if voucher < 0:
            break
        else:
            counterTickets += 1
    else:
        expences = ord(inputLine[0])
        voucher -= expences
        if voucher < 0:
            break
        else:
            counterOthers += 1
    inputLine = input()


print(counterTickets)
print(counterOthers)
