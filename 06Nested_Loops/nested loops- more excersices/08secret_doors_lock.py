first=int(input())
second=int(input())
thirth=int(input())

ten=[2,3,5,7]

for i in range(2,first+1,2):
    for l in range(1,second+1):
        for j in range(2, thirth+1,2):
            if l in ten:
                print(i,l,j)