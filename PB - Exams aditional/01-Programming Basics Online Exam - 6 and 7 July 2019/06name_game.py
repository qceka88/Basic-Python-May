input_line = input()
word = 0
cur_winner = ""
total_score = 0
winner=False
while input_line != "Stop":
    current_score = 0
    for character in input_line:
        input_number = int(input())
        word = ord(character)
        if word == input_number:
            current_score += 10
        elif word != input_number:
            current_score += 2
    if total_score<=current_score:
        total_score=current_score
        cur_winer = input_line
        winner=True

    input_line = input()

if winner:
    print(f"The winner is {cur_winer} with {total_score} points!")
