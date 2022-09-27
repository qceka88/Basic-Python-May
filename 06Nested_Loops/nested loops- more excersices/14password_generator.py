num01=int(input())
num02=int(input())

letter=97+num02

for i in range(1,num01):
    for j in range(1,num01):
        for k in range(97,letter):
            for l in range(97,letter):
                for m in range(1,num01+1):
                    if i< m and j <m:
                        print(f"{i}{j}{chr(k)}{chr(l)}{m}", end=" ")