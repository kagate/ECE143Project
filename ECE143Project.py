'''ECE 143 Project'''

import csv
import numpy as np
from collections import Counter

# Other functions
import platform_plots

# load MoviesOnStreamingPlatforms csv and IMDBMovieData csv
MoviesData = []
with open('/Users/laurabecerra/code/finalproject/ECE143Project/MoviesOnStreamingPlatforms_updated.csv', encoding="utf8") as MoviesCSVFile:
    MoviesCSVReader = csv.reader(MoviesCSVFile)
    MovieData = list(MoviesCSVReader)
    NumMovies = len(MovieData)

TVshowData = []
with open('/Users/laurabecerra/code/finalproject/ECE143Project/tv_shows.csv', encoding="utf8") as TVshowsCSVFile:
    TVshowsCSVReader = csv.reader(TVshowsCSVFile)
    TVshowData = list(TVshowsCSVReader)
    NumTVshows = len(TVshowData)

IMDBData = []
with open('/Users/laurabecerra/code/finalproject/ECE143Project/IMDB-Movie-Data.csv', encoding="utf8") as IMDBDataFile:
    IMDBDataReader = csv.reader(IMDBDataFile)
    IMDBData = list(IMDBDataReader)

# Adjust age ratings data so that if there is no age rating entry, it is replaced with "not rated"
AdjustedMovieData = [['not rated' if all([not AgeRating, i == 4]) else AgeRating for i, AgeRating in enumerate(MovieEntry)] for MovieEntry in MovieData[1:]]
AdjustedTVshowData = [['not rated' if all([not AgeRating, i == 3]) else AgeRating for i, AgeRating in enumerate(TVshowEntry)] for TVshowEntry in TVshowData[1:]]

# Extract and plot data on age ratings
# ----------------------------------------------------------------------------------------------------------------------------------
#Movie age ratings
NetflixAgeRatingsTemp = [row[4] for row in AdjustedMovieData if int(row[7]) == 1]
HuluAgeRatingsTemp = [row[4] for row in AdjustedMovieData if int(row[8]) == 1]
PrimeAgeRatingsTemp = [row[4] for row in AdjustedMovieData if int(row[9]) == 1]
DisneyAgeRatingsTemp = [row[4] for row in AdjustedMovieData if int(row[10]) == 1]

#TV Show age ratings
NetflixAgeRatingsTemp_TVshow = [row[3] for row in AdjustedTVshowData if int(row[6]) == 1]
HuluAgeRatingsTemp_TVshow = [row[3] for row in AdjustedTVshowData if int(row[7]) == 1]
PrimeAgeRatingsTemp_TVshow = [row[3] for row in AdjustedTVshowData if int(row[8]) == 1]
DisneyAgeRatingsTemp_TVshow = [row[3] for row in AdjustedTVshowData if int(row[9]) == 1]

# Make pie chart of movie age ratings, consider empty data entries as unrated films
# Netflix plot movies
NetflixAgesDict = Counter(NetflixAgeRatingsTemp)
platform_plots.pie_charts(NetflixAgesDict, "Netflix Movie Age Ratings", "NetflixAgeRatingsChart.png")

# Netflix plot TV shows
NetflixAgesTVshowDict = Counter(NetflixAgeRatingsTemp_TVshow)
platform_plots.pie_charts(NetflixAgesTVshowDict, "Netflix TV Show Age Ratings", "NetflixTVShowAgeRatingsChart.png")

# Hulu Plot movies
HuluAgesDict = Counter(HuluAgeRatingsTemp)
platform_plots.pie_charts(HuluAgesDict, "Hulu Movie Age Ratings", "HuluAgeRatingsChart.png")

# Hulu Plot TV shows
HuluAgesTVshowDict = Counter(HuluAgeRatingsTemp_TVshow)
platform_plots.pie_charts(HuluAgesTVshowDict, "Hulu TV Show Age Ratings", "HuluTVShowAgeRatingsChart.png")

# Prime Plot movies
PrimeAgesDict = Counter(PrimeAgeRatingsTemp)
platform_plots.pie_charts(PrimeAgesDict, "Prime Movie Age Ratings", "PrimeAgeRatingsChart.png")

# Prime Plot TV shows
PrimeAgesTVshowDict = Counter(PrimeAgeRatingsTemp_TVshow)
platform_plots.pie_charts(PrimeAgesTVshowDict, "Prime TV Show Age Ratings", "PrimeTVShowAgeRatingsChart.png")

# Disney Plot movies
DisneyAgesDict = Counter(DisneyAgeRatingsTemp)
platform_plots.pie_charts(DisneyAgesDict, "Disney Movie Age Ratings", "DisneyAgeRatingsChart.png")

# Disney Plot TV shows
DisneyAgesTVshowDict = Counter(DisneyAgeRatingsTemp_TVshow)
platform_plots.pie_charts(DisneyAgesTVshowDict, "Disney TV Show Age Ratings", "DisneyTVShowAgeRatingsChart.png")
# ----------------------------------------------------------------------------------------------------------------------------------

# Extract and plot movie genre data
# ----------------------------------------------------------------------------------------------------------------------------------
NetflixGenresTemp = [row[13].split(',') for row in AdjustedMovieData if int(row[7]) == 1]
HuluGenresTemp = [row[13].split(',') for row in AdjustedMovieData if int(row[8]) == 1]
PrimeGenresTemp = [row[13].split(',') for row in AdjustedMovieData if int(row[9]) == 1]
DisneyGenresTemp = [row[13].split(',') for row in AdjustedMovieData if int(row[10]) == 1]

# Flattens the nested lists, so that usage of Counter is possible
NetflixGenres = sum(NetflixGenresTemp, [])
HuluGenres = sum(HuluGenresTemp, [])
PrimeGenres = sum(PrimeGenresTemp, [])
DisneyGenres = sum(DisneyGenresTemp, [])

# Netflix Plot
NetflixGenresDict = Counter(NetflixGenres)
DictSize = len(NetflixGenresDict)
ExplodeListNetflix = [0.1]*DictSize
platform_plots.pie_charts(NetflixGenresDict, "Netflix Movies Genres", "NetflixMoviesGenres.png", ExplodeListNetflix)

# Hulu Plot
HuluGenresDict = Counter(HuluGenres)
DictSize = len(HuluGenresDict)
ExplodeListHulu = [0.1]*DictSize
platform_plots.pie_charts(HuluGenresDict, "Hulu Movies Genres", "HuluMoviesGenres.png", ExplodeListHulu)

# Prime Plot
PrimeGenresDict = Counter(PrimeGenres)
DictSize = len(PrimeGenresDict)
ExplodeListPrime = [0.1]*DictSize
platform_plots.pie_charts(PrimeGenresDict, "Prime Movies Genres", "PrimeMoviesGenres.png", ExplodeListPrime)

# Disney Plot
DisneyGenresDict = Counter(DisneyGenres)
DictSize = len(DisneyGenresDict)
ExplodeListDisney = [0.1]*DictSize
platform_plots.pie_charts(DisneyGenresDict, "Disney Movies Genres", "DisneyMoviesGenres.png", ExplodeListDisney)

# ----------------------------------------------------------------------------------------------------------------------------------

# Extract and plot IMDB ratings
# ----------------------------------------------------------------------------------------------------------------------------------
# Movies
NetflixIMDBScores = [float(row[5]) for row in AdjustedMovieData if int(row[7]) == 1 if row[5]]
HuluIMDBScores = [float(row[5]) for row in AdjustedMovieData if int(row[8]) == 1 if row[5]]
PrimeIMDBScores = [float(row[5]) for row in AdjustedMovieData if int(row[9]) == 1 if row[5]]
DisneyIMDBScores = [float(row[5]) for row in AdjustedMovieData if int(row[10]) == 1 if row[5]]

# TV Shows
NetflixIMDBTVshowScores = [float(row[4]) for row in AdjustedTVshowData if int(row[6]) == 1 if row[4]]
HuluIMDBTVshowScores = [float(row[4]) for row in AdjustedTVshowData if int(row[7]) == 1 if row[4]]
PrimeIMDBTVshowScores = [float(row[4]) for row in AdjustedTVshowData if int(row[8]) == 1 if row[4]]
DisneyIMDBTVshowScores = [float(row[4]) for row in AdjustedTVshowData if int(row[9]) == 1 if row[4]]

# Make new age lists which don't include data points that don't have an IMDB score
# Movies
NetflixIMDBAges = [row[4] for row in AdjustedMovieData if int(row[7]) == 1 if row[5]]
HuluIMDBAges = [row[4] for row in AdjustedMovieData if int(row[8]) == 1 if row[5]]
PrimeIMDBAges = [row[4] for row in AdjustedMovieData if int(row[9]) == 1 if row[5]]
DisneyIMDBAges = [row[4] for row in AdjustedMovieData if int(row[10]) == 1 if row[5]]

# TV Shows
NetflixIMDBTVshowAges = [row[3] for row in AdjustedTVshowData if int(row[6]) == 1 if row[4]]
HuluIMDBTVshowAges = [row[3] for row in AdjustedTVshowData if int(row[7]) == 1 if row[4]]
PrimeIMDBTVshowAges = [row[3] for row in AdjustedTVshowData if int(row[8]) == 1 if row[4]]
DisneyIMDBTVshowAges = [row[3] for row in AdjustedTVshowData if int(row[9]) == 1 if row[4]]

# Gather all platform IMDB scores and ages
IMDBMovieScores = [NetflixIMDBScores, HuluIMDBScores, PrimeIMDBScores, DisneyIMDBScores]
IMDBMovieAges = [NetflixIMDBAges, HuluIMDBAges, PrimeIMDBAges, DisneyIMDBAges]
IMDBTVshowScores = [NetflixIMDBTVshowScores, HuluIMDBTVshowScores, PrimeIMDBTVshowScores, DisneyIMDBTVshowScores]
IMDBTVshowAges = [NetflixIMDBTVshowAges, HuluIMDBTVshowAges, PrimeIMDBTVshowAges, DisneyIMDBTVshowAges]

platform_plots.scatter_plots(IMDBMovieScores, "IMDB Movie Scores", 'IMDBScoresScatterPlot.png', IMDBMovieAges, "Ages")
platform_plots.scatter_plots(IMDBTVshowScores, "IMDB TV Show Scores", 'IMDBTVShowScoresScatterPlot.png', IMDBTVshowAges, "Ages")
# ----------------------------------------------------------------------------------------------------------------------------------

# Extract and plot Rotten Tomato ratings
# ----------------------------------------------------------------------------------------------------------------------------------
# Movies
NetflixRTScores = [float(row[6].replace('%', '')) for row in AdjustedMovieData if int(row[7]) == 1 if row[6]]
HuluRTScores = [float(row[6].replace('%', '')) for row in AdjustedMovieData if int(row[8]) == 1 if row[6]]
PrimeRTScores = [float(row[6].replace('%', '')) for row in AdjustedMovieData if int(row[9]) == 1 if row[6]]
DisneyRTScores = [float(row[6].replace('%', '')) for row in AdjustedMovieData if int(row[10]) == 1 if row[6]]

# TV Shows
NetflixRTTVshowScores = [float(row[5].replace('%', '')) for row in AdjustedTVshowData if int(row[6]) == 1 if row[5]]
HuluRTTVshowScores = [float(row[5].replace('%', '')) for row in AdjustedTVshowData if int(row[7]) == 1 if row[5]]
PrimeRTTVshowScores = [float(row[5].replace('%', '')) for row in AdjustedTVshowData if int(row[8]) == 1 if row[5]]
DisneyRTTVshowScores = [float(row[5].replace('%', '')) for row in AdjustedTVshowData if int(row[9]) == 1 if row[5]]

# Make new age lists which don't include data points that don't have an IMDB score
# Movies
NetflixRTAges = [row[4] for row in AdjustedMovieData if int(row[7]) == 1 if row[6]]
HuluRTAges = [row[4] for row in AdjustedMovieData if int(row[8]) == 1 if row[6]]
PrimeRTAges = [row[4] for row in AdjustedMovieData if int(row[9]) == 1 if row[6]]
DisneyRTAges = [row[4] for row in AdjustedMovieData if int(row[10]) == 1 if row[6]]

# TV Shows
NetflixRTTVshowAges = [row[3] for row in AdjustedTVshowData if int(row[6]) == 1 if row[5]]
HuluRTTVshowAges = [row[3] for row in AdjustedTVshowData if int(row[7]) == 1 if row[5]]
PrimeRTTVshowAges = [row[3] for row in AdjustedTVshowData if int(row[8]) == 1 if row[5]]
DisneyRTTVshowAges = [row[3] for row in AdjustedTVshowData if int(row[9]) == 1 if row[5]]

# Gather all platform Rottem Tomato scores and ages
RTMovieScores = [NetflixRTScores, HuluRTScores, PrimeRTScores, DisneyRTScores]
RTMovieAges = [NetflixRTAges, HuluRTAges, PrimeRTAges, DisneyRTAges]
RTTVshowScores = [NetflixRTTVshowScores, HuluRTTVshowScores, PrimeRTTVshowScores, DisneyRTTVshowScores]
RTTVshowAges = [NetflixRTTVshowAges, HuluRTTVshowAges, PrimeRTTVshowAges, DisneyRTTVshowAges]

platform_plots.scatter_plots(RTMovieScores, "Rotten Tomato Movie Scores", 'RottenTomatoScoresScatterPlot.png', RTMovieAges, "Ages")
platform_plots.scatter_plots(RTTVshowScores, "Rotten Tomato TV Show Scores", 'RottenTomatoTVShowScoresScatterPlot.png', RTTVshowAges, "Ages")
# ----------------------------------------------------------------------------------------------------------------------------------

# Make plot showing which streaming platforms have the 1000 most popular movies (according to IMDB)
# ----------------------------------------------------------------------------------------------------------------------------------
# The goal figure here was to have a rectangular grid where each row represents a movie on the 1000 most popular movies list
# and each column represents a streaming platform.  A grid square will be filled in with one color if the streaming platform 
# has the movie or filled in with a different color if the streaming platform does not have the movie.

# Only plot first 30 most popular movies for now (for plot spacing reasons)
MaxEntry = 30
MostPopMovies = [row[1] for row in IMDBData[1:]]

NetflixMovies = [row[2] for row in AdjustedMovieData if int(row[7]) == 1]
PrimeMovies = [row[2] for row in AdjustedMovieData if int(row[8]) == 1]
HuluMovies = [row[2] for row in AdjustedMovieData if int(row[9]) == 1]
DisneyMovies = [row[2] for row in AdjustedMovieData if int(row[10]) == 1]

NetflixPopMovies = [1.0 if movie in NetflixMovies else 0.0 for movie in MostPopMovies]
PrimePopMovies = [1.0 if movie in PrimeMovies else 0.0 for movie in MostPopMovies]
HuluPopMovies = [1.0 if movie in HuluMovies else 0.0 for movie in MostPopMovies]
DisneyPopMovies = [1.0 if movie in DisneyMovies else 0.0 for movie in MostPopMovies]

TempList = [NetflixPopMovies[0:MaxEntry], PrimePopMovies[0:MaxEntry], HuluPopMovies[0:MaxEntry], DisneyPopMovies[0:MaxEntry]]
PopMoviesArray = np.asarray(TempList, dtype=np.float32)

StreamingPlatformsList = ["Netflix", "Prime", "Hulu", "Disney+"]
platform_plots.heatmap_plots(np.transpose(PopMoviesArray), MostPopMovies[0:MaxEntry], StreamingPlatformsList, "PopularMoviesHeatmap.png")

# ----------------------------------------------------------------------------------------------------------------------------------

# Bar graph of # of popular movies each streaming platform has
# ----------------------------------------------------------------------------------------------------------------------------------
NetflixPopMoviesCount = sum(NetflixPopMovies)
HuluPopMoviesCount = sum(HuluPopMovies)
PrimePopMoviesCount = sum(PrimePopMovies)
DisneyPopMoviesCount = sum(DisneyPopMovies)

PopMoviesCount = [NetflixPopMoviesCount, HuluPopMoviesCount, PrimePopMoviesCount, DisneyPopMoviesCount]
Data1Name = "Popular Movies Count"
Filename="BarChartPopMoviesCount.png"

platform_plots.bar_charts(StreamingPlatformsList, PopMoviesCount, Data1Name, Filename)
