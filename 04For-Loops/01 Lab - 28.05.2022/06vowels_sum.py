some_text= input()
sum_of_points=0
for letter in some_text:
    if letter == "a":
        sum_of_points += 1
    elif letter == "e":
        sum_of_points += 2
    elif letter == "i":
        sum_of_points += 3
    elif letter == "o":
        sum_of_points += 4
    elif letter == "u":
        sum_of_points += 5
print(sum_of_points)
