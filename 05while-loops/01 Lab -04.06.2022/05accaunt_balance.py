total_sum=0
command=input()

while command != "NoMoreMoney":
    current_sum=float(command)
    if current_sum<0:
        print("Invalid operation!")
        break
    print(f"Increase: {current_sum:.2f}")
    total_sum+=current_sum
    command=input()

print(f"Total: {total_sum:.2f}")