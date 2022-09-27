pool_v = int(input())
pipe1 = int(input())
pipe2 = int(input())
hours = float(input())
water_total = (pipe2 + pipe1) * hours
if water_total <= pool_v:
    water_percent= water_total / pool_v * 100
    pipe1_percent=(pipe1*hours)/water_total*100
    pipe2_percent=(pipe2*hours)/water_total*100
    print(f"The pool is {water_percent:.2f}% full. Pipe 1: {pipe1_percent:.2f}%. Pipe 2: {pipe2_percent:.2f}%.")
else:
    overflow = water_total - pool_v
    print(f"For {hours} hours the pool overflows with {overflow:.2f} litters")
