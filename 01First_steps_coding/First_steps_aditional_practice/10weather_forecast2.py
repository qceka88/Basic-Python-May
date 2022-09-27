temperature = float(input())
if 26 <= temperature <= 35:
    print('Hot')
elif 20.1 <= temperature <= 25.9:
    print('Warm')
elif 15.0 <= temperature <= 20:
    print('Mild')
elif 12 <= temperature <= 14.9:
    print('Cool')
elif 5 <= temperature <= 11.9:
    print('Cold')
else:
    print('unknown')
