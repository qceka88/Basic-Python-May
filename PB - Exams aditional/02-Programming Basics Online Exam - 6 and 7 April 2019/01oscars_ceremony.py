rent_of_hall=int(input())

oscar_statue_price= rent_of_hall*0.7
catering_price= oscar_statue_price*0.85
sounding=catering_price/2


total_price=rent_of_hall+catering_price+sounding+oscar_statue_price

print(f"{total_price:.2f}")