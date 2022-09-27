control = int(input())

secret_a = 0
secret_b = 0
secret_c = 0
secret_d = 0
counter = 0
found_secret = False
for a in range(1, 9 + 1):
    for b in range(1, 9 + 1):
        for c in range(1, 9 + 1):
            for d in range(1, 9 + 1):
                if a < b and c > d and (a * b + c * d) == control:
                    print(f"{a}{b}{c}{d}", end=" ")
                    counter += 1
                    if counter == 4:
                        found_secret = True
                        secret_a = a
                        secret_b = b
                        secret_c = c
                        secret_d = d
                        continue

if found_secret:
    print()
    print(f"Password: {secret_a}{secret_b}{secret_c}{secret_d}")
else:
    print()
    print("No!")
