comand = input()

word = ""
n_count = 0
o_count = 0
c_count = 0

while comand != "End":
    letter = ord(comand)
    cur_letter = 0
    if 65 <= letter <= 90 or 97 <= letter <= 122:
        if letter == 110 and n_count < 1:  # n
            n_count += 1
        elif letter == 111 and o_count < 1:  # o
            o_count += 1
        elif letter == 99 and c_count < 1:  # c
            c_count += 1
        else:
            cur_letter = letter
            word += chr(cur_letter)
    if n_count == 1 and c_count == 1 and o_count == 1:
        print(word, end=" ")
        n_count = 0
        c_count = 0
        o_count = 0
        word=""
    comand = input()
