'''ECE 143 Project'''

import csv
import numpy as np
from collections import Counter
from collections import OrderedDict
from pprint import pprint as pp
import circlify as circ

# Other functions
import platform_plots
import movie_plots

# load MoviesOnStreamingPlatforms csv and IMDBMovieData csv
MovieData = []
with open('C:/Users/felyl/Documents/ECE143/ProjectData/MoviesOnStreamingPlatforms_updated.csv', encoding="utf8") as MoviesCSVFile:
    MoviesCSVReader = csv.reader(MoviesCSVFile)
    MovieData = list(MoviesCSVReader)
    NumMovies = len(MovieData)

TVshowData = []
with open('C:/Users/felyl/Documents/ECE143/ProjectData/TV_shows_all_features.csv', encoding="utf8") as TVshowsCSVFile:
    TVshowsCSVReader = csv.reader(TVshowsCSVFile)
    TVshowData = list(TVshowsCSVReader)
    NumTVshows = len(TVshowData)

IMDBData = []
with open('C:/Users/felyl/Documents/ECE143/ProjectData/IMDB-Movie-Data.csv', encoding="utf8") as IMDBDataFile:
    IMDBDataReader = csv.reader(IMDBDataFile)
    IMDBData = list(IMDBDataReader)

# Adjust age ratings data so that if there is no age rating entry, it is replaced with "not rated"
AdjustedMovieData = [['not rated' if all([not AgeRating, i == 4]) else AgeRating for i, AgeRating in enumerate(MovieEntry)] for MovieEntry in MovieData[1:]]
AdjustedTVshowData_1 = [['not rated' if all([not AgeRating, i == 2]) else AgeRating for i, AgeRating in enumerate(TVshowEntry)] for TVshowEntry in TVshowData[1:]]
AdjustedTVshowData = [['unknown' if all([not genre, i == 11]) else genre for i, genre in enumerate(TVshowEntry)] for TVshowEntry in AdjustedTVshowData_1[1:]]

# Extract and plot data on age ratings
# ----------------------------------------------------------------------------------------------------------------------------------
#Movie age ratings
NetflixAgeRatingsTemp = [row[4] for row in AdjustedMovieData if int(row[7]) == 1]
HuluAgeRatingsTemp = [row[4] for row in AdjustedMovieData if int(row[8]) == 1]
PrimeAgeRatingsTemp = [row[4] for row in AdjustedMovieData if int(row[9]) == 1]
DisneyAgeRatingsTemp = [row[4] for row in AdjustedMovieData if int(row[10]) == 1]

#TV Show age ratings
NetflixAgeRatingsTemp_TVshow = [row[3] for row in AdjustedTVshowData if row[5] == "TRUE"]
HuluAgeRatingsTemp_TVshow = [row[3] for row in AdjustedTVshowData if row[6] == "TRUE"]
PrimeAgeRatingsTemp_TVshow = [row[3] for row in AdjustedTVshowData if row[7] == "TRUE"]
DisneyAgeRatingsTemp_TVshow = [row[3] for row in AdjustedTVshowData if row[8] == "TRUE"]

# Make pie chart of movie age ratings, consider empty data entries as unrated films
# Netflix plot movies
NetflixAgesDict = Counter(NetflixAgeRatingsTemp)

# Netflix plot TV shows
NetflixAgesTVshowDict = Counter(NetflixAgeRatingsTemp_TVshow)
platform_plots.pie_charts(NetflixAgesTVshowDict, "Netflix TV Show Age Ratings", "NetflixTVShowAgeRatingsChart.png")

# Hulu Plot movies
HuluAgesDict = Counter(HuluAgeRatingsTemp)

# Hulu Plot TV shows
HuluAgesTVshowDict = Counter(HuluAgeRatingsTemp_TVshow)
platform_plots.pie_charts(HuluAgesTVshowDict, "Hulu TV Show Age Ratings", "HuluTVShowAgeRatingsChart.png")

# Prime Plot movies
PrimeAgesDict = Counter(PrimeAgeRatingsTemp)

# Prime Plot TV shows
PrimeAgesTVshowDict = Counter(PrimeAgeRatingsTemp_TVshow)
platform_plots.pie_charts(PrimeAgesTVshowDict, "Prime TV Show Age Ratings", "PrimeTVShowAgeRatingsChart.png")

# Disney Plot movies
DisneyAgesDict = Counter(DisneyAgeRatingsTemp)

movie_plots.movie_pie_charts(NetflixAgesDict, HuluAgesDict, PrimeAgesDict, DisneyAgesDict, "Streaming Platform Age Ratings", "PlatformAgeRatings", 4, ExplodeList=[])

# Disney Plot TV shows
DisneyAgesTVshowDict = Counter(DisneyAgeRatingsTemp_TVshow)
platform_plots.pie_charts(DisneyAgesTVshowDict, "Disney TV Show Age Ratings", "DisneyTVShowAgeRatingsChart.png")

# ----------------------------------------------------------------------------------------------------------------------------------

# Extract and plot genre data
# ----------------------------------------------------------------------------------------------------------------------------------
# Movies
NetflixGenresTemp_movie = [row[13].split(',') for row in AdjustedMovieData if int(row[7]) == 1]
HuluGenresTemp_movie = [row[13].split(',') for row in AdjustedMovieData if int(row[8]) == 1]
PrimeGenresTemp_movie = [row[13].split(',') for row in AdjustedMovieData if int(row[9]) == 1]
DisneyGenresTemp_movie = [row[13].split(',') for row in AdjustedMovieData if int(row[10]) == 1]

# TV Shows
AdjustedTVshowDataGenres = [row for row in AdjustedTVshowData if len(row) == 12]
NetflixGenresTemp_TVShow = [row[11].split(',') for row in AdjustedTVshowDataGenres if row[5] == "TRUE"]
HuluGenresTemp_TVShow = [row[11].split(',') for row in AdjustedTVshowDataGenres if row[6] == "TRUE"]
PrimeGenresTemp_TVShow = [row[11].split(',') for row in AdjustedTVshowDataGenres if row[7] == "TRUE"]
DisneyGenresTemp_TVShow = [row[11].split(',') for row in AdjustedTVshowDataGenres if row[8] == "TRUE"]

# Flattens the nested lists, so that usage of Counter is possible
NetflixMovieGenres = sum(NetflixGenresTemp_movie, [])
HuluMovieGenres = sum(HuluGenresTemp_movie, [])
PrimeMovieGenres = sum(PrimeGenresTemp_movie, [])
DisneyMovieGenres = sum(DisneyGenresTemp_movie, [])

NetflixTVShowGenres = sum(NetflixGenresTemp_TVShow, [])
HuluTVShowGenres = sum(HuluGenresTemp_TVShow, [])
PrimeTVShowGenres = sum(PrimeGenresTemp_TVShow, [])
DisneyTVShowGenres = sum(DisneyGenresTemp_TVShow, [])

# Netflix Plot
Order = ['Action', 'Documentary', 'Adventure', 'Musical', 'Thriller', 'Sci-Fi', 'Sport', \
     'Comedy', 'History', 'Short', 'Western', 'Family', 'News', 'Animation', 'War', \
         'Drama', 'Crime', 'Music', 'Fantasy', 'Film-Noir', 'Horror', 'Romance', 'Reality-TV']
NetflixGenresDict = Counter(NetflixMovieGenres)
# Order netflix dictionary 
NetflixOrderedDict = OrderedDict()
for genre in Order:
    NetflixOrderedDict[genre] = NetflixGenresDict[genre]
DictSize = len(NetflixOrderedDict)
ExplodeListNetflix = [0.005]*DictSize

# Hulu Plot
HuluGenresDict = Counter(HuluMovieGenres)
HuluOrderedDict = OrderedDict()
for genre in Order:
    HuluOrderedDict[genre] = HuluGenresDict[genre]
DictSize = len(HuluOrderedDict)
ExplodeListHulu = [0.005]*DictSize

# Prime Plot
PrimeGenresDict = Counter(PrimeMovieGenres)
PrimeOrderedDict = OrderedDict()
for genre in Order:
    PrimeOrderedDict[genre] = PrimeGenresDict[genre]
DictSize = len(PrimeOrderedDict)
ExplodeListPrime = [0.005]*DictSize

# Disney Plot
DisneyGenresDict = Counter(DisneyMovieGenres)
DisneyOrderedDict = OrderedDict()
# Make disney order.  Note it's different because disney+ contains a subset of the genres on the other three streaming platforms
DisneyOrder = [genre for genre in Order if DisneyGenresDict.__contains__(genre)]
for genre in DisneyOrder:
    DisneyOrderedDict[genre] = DisneyGenresDict[genre]
DictSize = len(DisneyOrderedDict)
ExplodeListDisney = [0.005]*DictSize
movie_plots.movie_pie_charts(NetflixOrderedDict, HuluOrderedDict, PrimeOrderedDict, DisneyOrderedDict, "Movies Genres", \
    "MoviesGenresPieChart", 2, [ExplodeListNetflix, ExplodeListHulu, ExplodeListPrime, ExplodeListDisney])

# Netflix TV Plot
NetflixTVShowGenresDict = Counter(NetflixTVShowGenres)
DictSize = len(NetflixTVShowGenresDict)
ExplodeListNetflix_TVShow = [0.1]*DictSize
platform_plots.pie_charts(NetflixTVShowGenresDict, "Netflix TV Shows Genres", "NetflixTVShowsGenres.png", ExplodeListNetflix_TVShow)

# Hulu TV Plot
HuluTVShowGenresDict = Counter(HuluTVShowGenres)
DictSize = len(HuluTVShowGenresDict)
ExplodeListHulu_TVShow = [0.1]*DictSize
platform_plots.pie_charts(HuluTVShowGenresDict, "Hulu TV Shows Genres", "HuluTVShowsGenres.png", ExplodeListHulu_TVShow)

# Prime TV Plot
PrimeTVShowGenresDict = Counter(PrimeTVShowGenres)
DictSize = len(PrimeTVShowGenresDict)
ExplodeListPrime_TVShow = [0.1]*DictSize
platform_plots.pie_charts(PrimeTVShowGenresDict, "Prime TV Shows Genres", "PrimeTVShowsGenres.png", ExplodeListPrime_TVShow)

# Disney TV Plot
DisneyTVShowGenresDict = Counter(DisneyTVShowGenres)
DictSize = len(DisneyTVShowGenresDict)
ExplodeListDisney_TVShow = [0.1]*DictSize
platform_plots.pie_charts(DisneyTVShowGenresDict, "Disney TV Shows Genres", "DisneyTVShowsGenres.png", ExplodeListDisney_TVShow)
# ----------------------------------------------------------------------------------------------------------------------------------

# Extract and plot IMDB ratings
# ----------------------------------------------------------------------------------------------------------------------------------
# Movies
NetflixIMDBScores = [float(row[5]) for row in AdjustedMovieData if int(row[7]) == 1 if row[5] if row[4] != "not rated" if row[4] != "16+"]
HuluIMDBScores = [float(row[5]) for row in AdjustedMovieData if int(row[8]) == 1 if row[5] if row[4] != "not rated" if row[4] != "16+"]
PrimeIMDBScores = [float(row[5]) for row in AdjustedMovieData if int(row[9]) == 1 if row[5] if row[4] != "not rated" if row[4] != "16+"]
DisneyIMDBScores = [float(row[5]) for row in AdjustedMovieData if int(row[10]) == 1 if row[5] if row[4] != "not rated" if row[4] != "16+"]

# TV Shows
NetflixIMDBTVshowScores = [float(row[3]) for row in AdjustedTVshowData if row[5] == "True" if row[3] if row[2] != "not rated" if row[2] != "16+"]
HuluIMDBTVshowScores = [float(row[3]) for row in AdjustedTVshowData if row[6] == "True" if row[3] if row[2] != "not rated" if row[2] != "16+"]
PrimeIMDBTVshowScores = [float(row[3]) for row in AdjustedTVshowData if row[7] == "True" if row[3] if row[2] != "not rated" if row[2] != "16+"]
DisneyIMDBTVshowScores = [float(row[3]) for row in AdjustedTVshowData if row[8] == "True" if row[3] if row[2] != "not rated" if row[2] != "16+"]

# Make new age lists which don't include data points that don't have an IMDB score or have an age rating of "not rated"
# Movies
NetflixIMDBAges = [row[4] for row in AdjustedMovieData if int(row[7]) == 1 if row[5] if row[4] != "not rated" if row[4] != "16+"]
HuluIMDBAges = [row[4] for row in AdjustedMovieData if int(row[8]) == 1 if row[5] if row[4] != "not rated" if row[4] != "16+"]
PrimeIMDBAges = [row[4] for row in AdjustedMovieData if int(row[9]) == 1 if row[5] if row[4] != "not rated" if row[4] != "16+"]
DisneyIMDBAges = [row[4] for row in AdjustedMovieData if int(row[10]) == 1 if row[5] if row[4] != "not rated" if row[4] != "16+"]

# TV Shows
NetflixIMDBTVshowAges = [row[2] for row in AdjustedTVshowData if row[5] == "True" if row[3] if row[2] != "not rated" if row[2] != "16+"]
HuluIMDBTVshowAges = [row[2] for row in AdjustedTVshowData if row[6] == "True" if row[3] if row[2] != "not rated" if row[2] != "16+"]
PrimeIMDBTVshowAges = [row[2] for row in AdjustedTVshowData if row[7] == "True" if row[3] if row[2] != "not rated" if row[2] != "16+"]
DisneyIMDBTVshowAges = [row[2] for row in AdjustedTVshowData if row[8] == "True" if row[3] if row[2] != "not rated" if row[2] != "16+"]

# Gather all platform IMDB scores and ages
IMDBMovieScores = [NetflixIMDBScores, HuluIMDBScores, PrimeIMDBScores, DisneyIMDBScores]
IMDBMovieAges = [NetflixIMDBAges, HuluIMDBAges, PrimeIMDBAges, DisneyIMDBAges]
IMDBTVshowScores = [NetflixIMDBTVshowScores, HuluIMDBTVshowScores, PrimeIMDBTVshowScores, DisneyIMDBTVshowScores]
IMDBTVshowAges = [NetflixIMDBTVshowAges, HuluIMDBTVshowAges, PrimeIMDBTVshowAges, DisneyIMDBTVshowAges]

MoviePlotFlag = 4
TVPlotFlag = 4

movie_plots.movie_scatter_plots(IMDBMovieScores, "IMDB Scores", 'IMDBMovieScoresScatterPlot', IMDBMovieAges, "Ages", MoviePlotFlag)
movie_plots.movie_scatter_plots(IMDBTVshowScores, "IMDB TV Show Scores", 'IMDBTVShowScoresScatterPlot.png', IMDBTVshowAges, "Ages", TVPlotFlag)
# ----------------------------------------------------------------------------------------------------------------------------------

# Extract and plot Rotten Tomato ratings
# ----------------------------------------------------------------------------------------------------------------------------------
# Movies
NetflixRTScores = [float(row[6].replace('%', '')) for row in AdjustedMovieData if int(row[7]) == 1 if row[6] if row[4] != "not rated" if row[4] != "16+"]
HuluRTScores = [float(row[6].replace('%', '')) for row in AdjustedMovieData if int(row[8]) == 1 if row[6] if row[4] != "not rated" if row[4] != "16+"]
PrimeRTScores = [float(row[6].replace('%', '')) for row in AdjustedMovieData if int(row[9]) == 1 if row[6] if row[4] != "not rated" if row[4] != "16+"]
DisneyRTScores = [float(row[6].replace('%', '')) for row in AdjustedMovieData if int(row[10]) == 1 if row[6] if row[4] != "not rated" if row[4] != "16+"]

# TV Shows
NetflixRTTVshowScores = [float(row[4].replace('%', '')) for row in AdjustedTVshowData if row[5] == "True" if row[4] if row[2] != "not rated" if row[2] != "16+"]
HuluRTTVshowScores = [float(row[4].replace('%', '')) for row in AdjustedTVshowData if row[6] == "True" if row[4] if row[2] != "not rated" if row[2] != "16+"]
PrimeRTTVshowScores = [float(row[4].replace('%', '')) for row in AdjustedTVshowData if row[7] == "True" if row[4] if row[2] != "not rated" if row[2] != "16+"]
DisneyRTTVshowScores = [float(row[4].replace('%', '')) for row in AdjustedTVshowData if row[8] == "True" if row[4] if row[2] != "not rated" if row[2] != "16+"]

# Make new age lists which don't include data points that don't have a Rotten Tomato score
# Movies
NetflixRTAges = [row[4] for row in AdjustedMovieData if int(row[7]) == 1 if row[6] if row[4] != "not rated" if row[4] != "16+"]
HuluRTAges = [row[4] for row in AdjustedMovieData if int(row[8]) == 1 if row[6] if row[4] != "not rated" if row[4] != "16+"]
PrimeRTAges = [row[4] for row in AdjustedMovieData if int(row[9]) == 1 if row[6] if row[4] != "not rated" if row[4] != "16+"]
DisneyRTAges = [row[4] for row in AdjustedMovieData if int(row[10]) == 1 if row[6] if row[4] != "not rated" if row[4] != "16+"]

# TV Shows
NetflixRTTVshowAges = [row[2] for row in AdjustedTVshowData if row[5] == "True" if row[4] if row[2] != "not rated" if row[2] != "16+"]
HuluRTTVshowAges = [row[2] for row in AdjustedTVshowData if row[6] == "True" if row[4] if row[2] != "not rated" if row[2] != "16+"]
PrimeRTTVshowAges = [row[2] for row in AdjustedTVshowData if row[7] == "True" if row[4] if row[2] != "not rated" if row[2] != "16+"]
DisneyRTTVshowAges = [row[2] for row in AdjustedTVshowData if row[8] == "True" if row[4] if row[2] != "not rated" if row[2] != "16+"]

# Gather all platform Rottem Tomato scores and ages
RTMovieScores = [NetflixRTScores, HuluRTScores, PrimeRTScores, DisneyRTScores]
RTMovieAges = [NetflixRTAges, HuluRTAges, PrimeRTAges, DisneyRTAges]
RTTVshowScores = [NetflixRTTVshowScores, HuluRTTVshowScores, PrimeRTTVshowScores, DisneyRTTVshowScores]
RTTVshowAges = [NetflixRTTVshowAges, HuluRTTVshowAges, PrimeRTTVshowAges, DisneyRTTVshowAges]

movie_plots.movie_scatter_plots(RTMovieScores, "Rotten Tomato Movie Scores", 'RottenTomatoScoresScatterPlot', RTMovieAges, "Ages", 4)
movie_plots.movie_scatter_plots(RTTVshowScores, "Rotten Tomato TV Show Scores", 'RottenTomatoTVShowScoresScatterPlot', RTTVshowAges, "Ages", 4)
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

# ----------------------------------------------------------------------------------------------------------------------------------

# Circlify plot of languages
# ----------------------------------------------------------------------------------------------------------------------------------
# Movies
NetflixMovieLanguages = sum([row[15].split(",") for row in AdjustedMovieData if int(row[7]) == 1 if row[15]], [])
HuluMovieLanguages = sum([row[15].split(",") for row in AdjustedMovieData if int(row[8]) == 1 if row[15]], [])
PrimeMovieLanguages = sum([row[15].split(",") for row in AdjustedMovieData if int(row[9]) == 1 if row[15]], [])
DisneyMovieLanguages = sum([row[15].split(",") for row in AdjustedMovieData if int(row[10]) == 1 if row[15]], [])

NetflixLanguageCountsTemp = Counter(NetflixMovieLanguages)
HuluLanguageCountsTemp = Counter(HuluMovieLanguages)
PrimeLanguageCountsTemp = Counter(PrimeMovieLanguages)
DisneyLanguageCountsTemp = Counter(DisneyMovieLanguages)
AllLanguages = set(sum([list(NetflixLanguageCountsTemp.keys()), 
                        list(HuluLanguageCountsTemp.keys()), 
                        list(PrimeLanguageCountsTemp.keys()), 
                        list(DisneyLanguageCountsTemp.keys())], [])) 
NetflixLanguageCounts = {key: NetflixLanguageCountsTemp[key] for key in AllLanguages if NetflixLanguageCountsTemp[key] >= 20 if key != "English"}
HuluLanguageCounts = {key: HuluLanguageCountsTemp[key] for key in AllLanguages if HuluLanguageCountsTemp[key] >= 20 if key != "English"}
PrimeLanguageCounts = {key: PrimeLanguageCountsTemp[key] for key in AllLanguages if PrimeLanguageCountsTemp[key] >= 20 if key != "English"}
DisneyLanguageCounts = {key: DisneyLanguageCountsTemp[key] for key in AllLanguages if DisneyLanguageCountsTemp[key] >= 20 if key != "English"}
# TV shows
NetflixTVLanguages = sum([row[14].split(",") for row in AdjustedTVshowData if row[5] == "True" if row[14]], [])
HuluTVLanguages = sum([row[14].split(",") for row in AdjustedTVshowData if row[6] == "True" if row[14]], [])
PrimeTVLanguages = sum([row[14].split(",") for row in AdjustedTVshowData if row[7] == "True" if row[14]], [])
DisneyTVLanguages = sum([row[14].split(",") for row in AdjustedTVshowData if row[8] == "True" if row[14]], [])

NetflixTVLanguageCountsTemp = Counter(NetflixTVLanguages)
HuluTVLanguageCountsTemp = Counter(HuluTVLanguages)
PrimeTVLanguageCountsTemp = Counter(PrimeTVLanguages)
DisneyTVLanguageCountsTemp = Counter(DisneyTVLanguages)
AllLanguagesTV = set(sum([list(NetflixLanguageCountsTemp.keys()), 
                        list(HuluLanguageCountsTemp.keys()), 
                        list(PrimeLanguageCountsTemp.keys()), 
                        list(DisneyLanguageCountsTemp.keys())], [])) 
NetflixTVLanguageCounts = {key: NetflixTVLanguageCountsTemp[key] for key in AllLanguagesTV if NetflixTVLanguageCountsTemp[key] >= 5 if key != "English"}
HuluTVLanguageCounts = {key: HuluTVLanguageCountsTemp[key] for key in AllLanguagesTV if HuluTVLanguageCountsTemp[key] >= 5 if key != "English"}
PrimeTVLanguageCounts = {key: PrimeTVLanguageCountsTemp[key] for key in AllLanguagesTV if PrimeTVLanguageCountsTemp[key] >= 5 if key != "English"}
DisneyTVLanguageCounts = {key: DisneyTVLanguageCountsTemp[key] for key in AllLanguagesTV if DisneyTVLanguageCountsTemp[key] >= 5 if key != "English"}

movie_plots.lollipop(NetflixLanguageCounts, HuluLanguageCounts, PrimeLanguageCounts, DisneyLanguageCounts, "MovieLanguageBarChart.png")
movie_plots.lollipop(NetflixTVLanguageCounts, HuluTVLanguageCounts, PrimeTVLanguageCounts, DisneyTVLanguageCounts, "TVLanguageBarChart.png")

data = [{'id': 'Netflix', 'datum': 0.25, 'children':NetflixLanguageCounts.values()},
        {'id': 'Hulu', 'datum': 0.25, 'children':HuluLanguageCounts.values()},
        {'id': 'Prime', 'datum': 0.25, 'children':PrimeLanguageCounts.values()},
        {'id': 'Disney', 'datum': 0.25, 'children':DisneyLanguageCounts.values()}]
circles = circ.circlify(data, show_enclosure=True)
circ.bubbles(circles=circles)

data = [
        0.05, {'id': 'a2', 'datum': 0.05},
        {'id': 'a0', 'datum': 0.8, 'children': [0.3, 0.2, 0.2, 0.1], },
        {'id': 'a1', 'datum': 0.1, 'children': [
            {'id': 'a1_1', 'datum': 0.05}, {'datum': 0.04}, 0.01],
        },
    ]