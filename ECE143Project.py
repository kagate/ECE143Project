'''ECE 143 Project'''

import csv
import numpy as np
from collections import Counter
from collections import OrderedDict

# Other functions
import platform_plots

# load MoviesOnStreamingPlatforms csv and IMDBMovieData csv
MovieData = []
with open('data/MoviesOnStreamingPlatforms_updated.csv', encoding="utf8") as MoviesCSVFile:
    MoviesCSVReader = csv.reader(MoviesCSVFile)
    MovieData = list(MoviesCSVReader)
    NumMovies = len(MovieData)

TVshowData = []
with open('data/TV_shows_all_features.csv', encoding="utf8") as TVshowsCSVFile:
    TVshowsCSVReader = csv.reader(TVshowsCSVFile)
    TVshowData = list(TVshowsCSVReader)
    NumTVshows = len(TVshowData)

IMDBData = []
with open('data/IMDB-Movie-Data.csv', encoding="utf8") as IMDBDataFile:
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
NetflixAgeRatingsTemp_TVshow = [row[2] for row in AdjustedTVshowData if row[5] == "True"]
HuluAgeRatingsTemp_TVshow = [row[2] for row in AdjustedTVshowData if row[6] == "True"]
PrimeAgeRatingsTemp_TVshow = [row[2] for row in AdjustedTVshowData if row[7] == "True"]
DisneyAgeRatingsTemp_TVshow = [row[2] for row in AdjustedTVshowData if row[8] == "True"]

# Make pie chart of movie age ratings, consider empty data entries as unrated films
# Plot movies
NetflixAgesDict = Counter(NetflixAgeRatingsTemp)
HuluAgesDict = Counter(HuluAgeRatingsTemp)
PrimeAgesDict = Counter(PrimeAgeRatingsTemp)
DisneyAgesDict = Counter(DisneyAgeRatingsTemp)
platform_plots.pie_charts(NetflixAgesDict, HuluAgesDict, PrimeAgesDict, DisneyAgesDict, "Streaming Platform Age Ratings", "MoviePlatformAgeRatings", 4, ExplodeList=[])


# Plot TV shows
NetflixAgesTVshowDict = Counter(NetflixAgeRatingsTemp_TVshow)
HuluAgesTVshowDict = Counter(HuluAgeRatingsTemp_TVshow)
PrimeAgesTVshowDict = Counter(PrimeAgeRatingsTemp_TVshow)
DisneyAgesTVshowDict = Counter(DisneyAgeRatingsTemp_TVshow)
platform_plots.pie_charts(NetflixAgesTVshowDict, HuluAgesTVshowDict, PrimeAgesTVshowDict, DisneyAgesTVshowDict, "Streaming Platform Age Ratings", "TVPlatformAgeRatings", 4, ExplodeList=[])

# ----------------------------------------------------------------------------------------------------------------------------------

# Extract and plot genre data
# ----------------------------------------------------------------------------------------------------------------------------------
# Movies
NetflixGenresTemp_movie = [row[13].split(',') for row in AdjustedMovieData if int(row[7]) == 1]
HuluGenresTemp_movie = [row[13].split(',') for row in AdjustedMovieData if int(row[8]) == 1]
PrimeGenresTemp_movie = [row[13].split(',') for row in AdjustedMovieData if int(row[9]) == 1]
DisneyGenresTemp_movie = [row[13].split(',') for row in AdjustedMovieData if int(row[10]) == 1]

# TV Shows
AdjustedTVshowDataGenres = [row for row in AdjustedTVshowData if row[13] != '[]']
NetflixGenresTemp_TVShow = [((((row[13].replace('[', '')).replace(']', '')).replace('\'', '')).replace(' ', '')).split(',') for row in AdjustedTVshowDataGenres if row[5] == "True"]
HuluGenresTemp_TVShow = [((((row[13].replace('[', '')).replace(']', '')).replace('\'', '')).replace(' ', '')).split(',') for row in AdjustedTVshowDataGenres if row[6] == "True"]
PrimeGenresTemp_TVShow = [((((row[13].replace('[', '')).replace(']', '')).replace('\'', '')).replace(' ', '')).split(',') for row in AdjustedTVshowDataGenres if row[7] == "True"]
DisneyGenresTemp_TVShow = [((((row[13].replace('[', '')).replace(']', '')).replace('\'', '')).replace(' ', '')).split(',') for row in AdjustedTVshowDataGenres if row[8] == "True"]

# Flattens the nested lists, so that usage of Counter is possible
NetflixMovieGenres = sum(NetflixGenresTemp_movie, [])
HuluMovieGenres = sum(HuluGenresTemp_movie, [])
PrimeMovieGenres = sum(PrimeGenresTemp_movie, [])
DisneyMovieGenres = sum(DisneyGenresTemp_movie, [])

NetflixTVShowGenres = sum(NetflixGenresTemp_TVShow, [])
HuluTVShowGenres = sum(HuluGenresTemp_TVShow, [])
PrimeTVShowGenres = sum(PrimeGenresTemp_TVShow, [])
DisneyTVShowGenres = sum(DisneyGenresTemp_TVShow, [])

Order = ['Action', 'Documentary', 'Adventure', 'Musical', 'Thriller', 'Sci-Fi', 'Sport', \
     'Comedy', 'History', 'Short', 'Western', 'Family', 'News', 'Animation', 'War', \
         'Drama', 'Crime', 'Music', 'Fantasy', 'Film-Noir', 'Horror', 'Romance', 'Reality-TV']
# Netflix Plot
NetflixGenresDict = Counter(NetflixMovieGenres)
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
platform_plots.pie_charts(NetflixOrderedDict, HuluOrderedDict, PrimeOrderedDict, DisneyOrderedDict, "Movies Genres", \
    "MoviesGenresPieChart", 1, [ExplodeListNetflix, ExplodeListHulu, ExplodeListPrime, ExplodeListDisney])

TVOrder = ['Drama', 'Travel', 'Children', 'Supernatural', 'Adventure', 'Music', 'Romance', 'Fantasy', 'Horror', \
           'Crime', 'Action', 'Sports', 'Family', 'Science-Fiction', 'Mystery', 'Comedy', 'Anime', 'History', 'Food']
# Netflix TV Plot
NetflixTVShowGenresDict = Counter(NetflixTVShowGenres)
NetflixTVOrderedDict = OrderedDict()
for genre in TVOrder:
    NetflixTVOrderedDict[genre] = NetflixTVShowGenresDict[genre]
DictSize = len(NetflixTVOrderedDict)
ExplodeListNetflixTV = [0.005]*DictSize

# Hulu TV Plot
HuluTVShowGenresDict = Counter(HuluTVShowGenres)
HuluTVOrderedDict = OrderedDict()
for genre in TVOrder:
    HuluTVOrderedDict[genre] = HuluTVShowGenresDict[genre]
DictSize = len(HuluTVOrderedDict)
ExplodeListHuluTV = [0.005]*DictSize

# Prime TV Plot
PrimeTVShowGenresDict = Counter(PrimeTVShowGenres)
PrimeTVOrderedDict = OrderedDict()
for genre in TVOrder:
    PrimeTVOrderedDict[genre] = PrimeTVShowGenresDict[genre]
DictSize = len(PrimeTVOrderedDict)
ExplodeListPrimeTV = [0.005]*DictSize

# Disney TV Plot
DisneyTVShowGenresDict = Counter(DisneyTVShowGenres)
DisneyTVOrderedDict = OrderedDict()
for genre in TVOrder:
    DisneyTVOrderedDict[genre] = DisneyTVShowGenresDict[genre]
DictSize = len(DisneyTVOrderedDict)
ExplodeListDisneyTV = [0.005]*DictSize

platform_plots.pie_charts(NetflixTVOrderedDict, HuluTVOrderedDict, PrimeTVOrderedDict, DisneyTVOrderedDict, "TV Show Genres", \
    "TVGenresPieChart", 1, [ExplodeListNetflixTV, ExplodeListHuluTV, ExplodeListPrimeTV, ExplodeListDisneyTV])
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

platform_plots.scatter_plots(IMDBMovieScores, "IMDB Scores", 'IMDBMovieScoresScatterPlot', IMDBMovieAges, "Ages", MoviePlotFlag)
platform_plots.scatter_plots(IMDBTVshowScores, "IMDB TV Show Scores", 'IMDBTVShowScoresScatterPlot.png', IMDBTVshowAges, "Ages", TVPlotFlag)
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

platform_plots.scatter_plots(RTMovieScores, "Rotten Tomato Movie Scores", 'RottenTomatoScoresScatterPlot', RTMovieAges, "Ages", 4)
platform_plots.scatter_plots(RTTVshowScores, "Rotten Tomato TV Show Scores", 'RottenTomatoTVShowScoresScatterPlot', RTTVshowAges, "Ages", 4)
# ----------------------------------------------------------------------------------------------------------------------------------

# Bar graph of # of popular movies each streaming platform has
# ----------------------------------------------------------------------------------------------------------------------------------
# uses the IMDB dataset which gives the 1000 most popular movies on IMDB.  This plot will be a bargraph showing how many of these 1000 most 
# popular movies each streaming platform has.  Note: a movie being on the 1000 most popular movies list is based on more than just the IMDB
# score, so this gives different info from just the IMDB scores on each streaming platform data we used earlier. 
MostPopMovies = [row[1] for row in IMDBData[1:]]

NetflixMovies = [row[2] for row in AdjustedMovieData if int(row[7]) == 1]
PrimeMovies = [row[2] for row in AdjustedMovieData if int(row[8]) == 1]
HuluMovies = [row[2] for row in AdjustedMovieData if int(row[9]) == 1]
DisneyMovies = [row[2] for row in AdjustedMovieData if int(row[10]) == 1]

NetflixPopMovies = [1.0 if movie in NetflixMovies else 0.0 for movie in MostPopMovies]
PrimePopMovies = [1.0 if movie in PrimeMovies else 0.0 for movie in MostPopMovies]
HuluPopMovies = [1.0 if movie in HuluMovies else 0.0 for movie in MostPopMovies]
DisneyPopMovies = [1.0 if movie in DisneyMovies else 0.0 for movie in MostPopMovies]

StreamingPlatformsList = ["Netflix", "Prime", "Hulu", "Disney+"]

NetflixPopMoviesCount = sum(NetflixPopMovies)
HuluPopMoviesCount = sum(HuluPopMovies)
PrimePopMoviesCount = sum(PrimePopMovies)
DisneyPopMoviesCount = sum(DisneyPopMovies)

PopMoviesCount = [NetflixPopMoviesCount, HuluPopMoviesCount, PrimePopMoviesCount, DisneyPopMoviesCount]
Data1Name = "Popular Movies Count"
Filename="BarChartPopMoviesCount.png"

platform_plots.bar_charts(StreamingPlatformsList, PopMoviesCount, Data1Name, Filename)

# ----------------------------------------------------------------------------------------------------------------------------------

# Stacked bar chart of languages
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

platform_plots.stacked_bar_chart(NetflixLanguageCounts, HuluLanguageCounts, PrimeLanguageCounts, DisneyLanguageCounts, "MovieLanguageBarChart.png")
platform_plots.stacked_bar_chart(NetflixTVLanguageCounts, HuluTVLanguageCounts, PrimeTVLanguageCounts, DisneyTVLanguageCounts, "TVLanguageBarChart.png")