command = input()
name = ""
bestMovie = 0
counter = 0

while command != "STOP":
    currentMovie = command
    counter += 1
    lenght = len(currentMovie)

    currentBestMovie = 0

    for i in currentMovie:
        currentLetter = ord(i)
        if 65 <= currentLetter <= 90:
            scores = currentLetter - lenght
            currentBestMovie += scores
        elif 97 <= currentLetter <= 122:
            scores = currentLetter - (lenght * 2)
            currentBestMovie += scores
        else:
            scores = currentLetter
            currentBestMovie += scores
    if currentBestMovie > bestMovie:
        bestMovie = currentBestMovie
        name = currentMovie
    if counter == 7:
        print("The limit is reached.")
        break
    command = input()
    if command == "STOP":
        break

print(f"The best movie for you is {name} with {bestMovie} ASCII sum.")
