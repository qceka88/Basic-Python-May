movieName = input()
daysQty = int(input())
ticketsQty = int(input())
priceTicket = float(input())
cinemaTax = int(input())

income = daysQty * ticketsQty * priceTicket

totalIncome = income - (cinemaTax * income / 100)

print(f"The profit from the movie {movieName} is {totalIncome:.2f} lv.")
