wanted_book = input()

book_count = 0
input_line = ""
needed_book = False
while input_line != "No More Books":
    input_line = input()
    current_book = input_line
    if input_line == "No More Books":
        break
    if current_book != wanted_book:
        book_count += 1
    else:
        needed_book = True
        break

if needed_book:
    print(f"You checked {book_count} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {book_count} books.")