looking_book = input()

input_line = input()
books_count = 0
is_book_found = False
while input_line != "No More Books":
    if input_line == looking_book:
        is_book_found = True
        break

    books_count += 1
    input_line = input()


if is_book_found:
    print(f"You checked {books_count} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {books_count} books.")