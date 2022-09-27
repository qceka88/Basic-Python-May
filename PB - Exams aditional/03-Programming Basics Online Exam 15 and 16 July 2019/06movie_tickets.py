a1 = int(input())
a2 = int(input())
n = int(input())
sym01=a2-1
sym03 = int(n / 2 - 1)
sym02 = n - 1
for i in range(a1, sym01+1):
    for j in range(1, sym02 + 1):
        for k in range(1, sym03 + 1):
            if i % 2 != 0 and (i + j + k) % 2 != 0:
                print(f"{chr(i)}-{j}{k}{i}")
