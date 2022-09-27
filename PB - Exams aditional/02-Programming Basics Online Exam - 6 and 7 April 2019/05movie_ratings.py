import sys

movieQty = int(input())

topMovieRating = -sys.maxsize
poorMovieRating = sys.maxsize
topMovieName = ""
poorMovieName = ""
totalRating = 0

for i in range(1, movieQty + 1):
    curMoviveName = input()
    curMoviveRating = float(input())
    totalRating += curMoviveRating

    if curMoviveRating >= topMovieRating:
        topMovieRating = curMoviveRating
        topMovieName = curMoviveName
    if curMoviveRating <= poorMovieRating:
        poorMovieRating = curMoviveRating
        poorMovieName = curMoviveName

averrageRating = totalRating / movieQty

print(f"{topMovieName} is with highest rating: {topMovieRating:.1f}")
print(f"{poorMovieName} is with lowest rating: {poorMovieRating:.1f}")
print(f"Average rating: {averrageRating:.1f}")
