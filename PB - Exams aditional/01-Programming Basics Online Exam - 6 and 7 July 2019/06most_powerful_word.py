from math import floor
import sys

input_word = input()
win_word = ""
total_score = -sys.maxsize
double_score = [65, 69, 73, 79, 85, 89, 97, 101, 105, 111, 117, 121]
while input_word != "End of words":
    current_score = 0
    bonus = len(input_word)
    first_character = ord(input_word[0])
    for character in input_word:
        current_score += ord(character)
    if first_character in double_score:
        current_score *= bonus
    elif first_character not in double_score:
        current_score = floor(current_score / bonus)
    if current_score > total_score:
        total_score = current_score
        win_word = input_word
        current_score=0

    input_word = input()
print(f"The most powerful word is {win_word} - {total_score}")
