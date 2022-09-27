seriesName = input()
seasonsQty = int(input())
episodesQty = int(input())
lenghtEpisode = float(input())


allEpisodes = seasonsQty * episodesQty * (lenghtEpisode*1.2)
lastEpizode = seasonsQty * 10
totalTime = allEpisodes + lastEpizode

print(f"Total time needed to watch the {seriesName} series is {round(totalTime)} minutes.")
